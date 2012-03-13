package com.criticalpath.seemonkey;

import java.awt.Rectangle;

import org.eclipse.swt.graphics.Point;
import org.sikuli.script.Debug;

import com.android.chimpchat.core.IChimpDevice;
import com.android.chimpchat.hierarchyviewer.HierarchyViewer;
import com.android.hierarchyviewerlib.device.ViewNode;


public class ViewManager {
	private static final String TAG = "ViewManager:";
	
	private IChimpDevice _device;
	private HierarchyViewer _viewer;

	private String _rootNodeActivity; // used to track when the view tree needs refreshing
	private ViewNode _rootNode; //speeds up accessing elements
	
	public ViewManager(IChimpDevice device) {
		_device = device;
		restartViewServer();
		try {
			_viewer = _device.getHierarchyViewer();
		} catch (Exception e) {
			Debug.error(TAG + "unable to debug device");
			_viewer = null;
		}
	}

    public HierarchyViewer getHierarchyViewer() {
    	return _viewer;
    }
    
    /*
     * uses the android `service` command to stop and restart the window service
     * on port 4939 (default)
     * using patterns ripped from hierarchyviewerlib.DeviceBridge
     */
    public void restartViewServer() {
    	this.restartViewServer(4939);
    }
    
    /*
     * uses the android `service` command to stop and restart the window service
     * using patterns ripped from hierarchyviewerlib.DeviceBridge
     * @param port port number to start the window service on 
     */
    public void restartViewServer(int port) {
    	try {
	    	final String START_SERVER = String.format("service call window %d i32 %d", 1, port); //$NON-NLS-1$
	    	Debug.info(TAG + String.format("starting window service on port %d", port));
	    	final String STOP_SERVER =  String.format("service call window %d", 2);
	        _device.shell(STOP_SERVER);
	        
	        // sleep(1000)
	        try {Thread.sleep(1000);} 
	        catch (InterruptedException e) {}
	        
	        _device.shell(START_SERVER);
    	 } catch (Exception e) {
    		 e.printStackTrace();
	     }
    }
    
    /**
     * checks if the device is debuggabler (i.e. a development build/rooted device)
     * @return True if device is debuggable
     */
    public Boolean isDeviceDebuggable() {
    	return (_viewer == null) ? false : true;
    }
    
    public String getFocusedWindowName() {
    	if (isDeviceDebuggable())
    		return _viewer.getFocusedWindowName();
    	else
    		return null;
    }

    /**
     * force refreshing of the current rootnode data by clearing the cached data
     */
    public void refresh() {
    	_rootNode = null;
    }
    
    /**
     * Checks to see if the current activity has changed and returns a cached copy of the rootnode data if 
     * the activity has not changed since the last time the rootnode was accessed
     * This speeds up successive node lookups on static uis as each new copy of rootnode takes 2-3 seconds to
     * complete.
     * 
     * @return ViewNode representing the rootnode (id/content)
     */
    private ViewNode getRootView() {
    	String currentActivity = getFocusedWindowName();
    	
    	if ((_rootNode == null) || (! _rootNodeActivity.equals(currentActivity))) {
    		Debug.info(TAG + "getting root view for " + currentActivity + "(was " + _rootNodeActivity + ")");
    		_rootNode = _viewer.findViewById("id/content");
    		_rootNodeActivity = currentActivity;
    	}
    	return _rootNode;
    }
    
    public ViewNode getViewById(String id) {
    	return _viewer.findViewById(id, getRootView());
    }
    
    public Rectangle getRectById(String id) {
    	// @+id/thisIsTheIdForTheView
    	try {
	    	ViewNode vn = getViewById(id);
	    	Point p = HierarchyViewer.getAbsolutePositionOfView(vn);
	    	Rectangle rect = new Rectangle(p.x, p.y, vn.width, vn.height);
	    	return rect;
    	} catch (Exception e) {
    		Debug.error(TAG + "view not found");
    		return null;
    	}
    }
    
    /**
     * Gets the text of a given element.
     *
     * @param selector selector for the view.
     * @return the text of the given element.
     */
    public String getTextById(String id) {
    	return getNamedPropertyById(id, "mText");
    }

    
    public String getNamedPropertyById(String id, String property) {
    	ViewNode node = getViewById(id);
        if (node == null) {
            throw new RuntimeException("Node not found");
        }
        
        if (property == null) {
        	return node.namedProperties.toString();
        }
        
        ViewNode.Property textProperty = node.namedProperties.get(property);
        if (textProperty == null) {
            throw new RuntimeException("No " + property + " property on node");
        }
        return textProperty.value;
    }
    
    

}
