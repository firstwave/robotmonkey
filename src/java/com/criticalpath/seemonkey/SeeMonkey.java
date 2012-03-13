package com.criticalpath.seemonkey;

import java.util.HashMap;
import java.util.TreeMap;

import org.sikuli.script.Debug;

import com.android.chimpchat.ChimpChat;
import com.android.chimpchat.core.IChimpDevice;

public class SeeMonkey {
	private static final String TAG = "SeeMonkey:";
	private static ChimpChat mChimpChat = null;
	private static HashMap<String, IChimpDevice> mDevices = new HashMap<String, IChimpDevice>();
	
	static {
		// set up the adb backend
		// try to get the path to adb from system properties
		String androidSdkAdbPath = System.getProperty("android.sdk.dir");
		if ( androidSdkAdbPath == null ) {
			mChimpChat = ChimpChat.getInstance(); //use default settings and hope for the best
		} else {
			TreeMap<String, String> options = new TreeMap<String, String>();	
			androidSdkAdbPath = androidSdkAdbPath + "/platform-tools/adb";
	        options.put("backend", "adb");
	        options.put("adbLocation", androidSdkAdbPath);
			mChimpChat = ChimpChat.getInstance(options);
		}
	}
	
	public static IChimpDevice waitForConnection(){
		return waitForConnection(-1, null);
	}
	
	public static IChimpDevice waitForConnection(long timeoutMs, String deviceId){
		IChimpDevice _device;
		
		if (deviceId == null) {
			Debug.info(TAG + "Waiting for connection to default device");
			if ((mDevices != null) && (mDevices.size() == 1))
				return mDevices.get(mDevices.keySet().toArray()[0]);
		} else {
			Debug.info(TAG + "Waiting for connection to device '" + deviceId + "'");
			if ((mDevices != null) && (mDevices.containsKey(deviceId)))
				return mDevices.get(deviceId);
		}
		Debug.info(TAG + "It is not unusual to see a com.android.ddmlib.ShellCommandUnresponsiveException");
	
		try{
			if(timeoutMs<0 || deviceId == null) {
				_device = mChimpChat.waitForConnection();
			} else {
				_device = mChimpChat.waitForConnection(timeoutMs, deviceId);
			}
			mDevices.put(deviceId, _device);
			return _device;
		}
		catch(Exception e){
			Debug.error(TAG + "Couldn't connect to device!");
			e.printStackTrace();
			return null;
		}
	}
}
