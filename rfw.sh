#!/bin/sh

RFW_LIBS="examples/ndtest/libs"
RFW_SUITE="examples/ndtest/data"

RFW_JAR="libs/robotframework-2.6.3.jar"
NATIVEDRIVER_JAR="client-standalone.jar"
NATIVEDRIVER_APP="com.paypal.android.p2pmobile"
XALAN_JAR="xalan-j_2_7_1/xalan.jar"

SIKULI_JAR="libs/sikuli-script.jar"
SEEMONKEY_JAR="libs/seemonkey.jar"

ANDROID_SDK="/Users/obartley/Library/android-sdk-macosx/tools/lib"
ANDROID_JARS="$ANDROID_SDK/guavalib.jar"
ANDROID_JARS="$ANDROID_JARS:$ANDROID_SDK/monkeyrunner.jar"
ANDROID_JARS="$ANDROID_JARS:$ANDROID_SDK/sdklib.jar"
ANDROID_JARS="$ANDROID_JARS:$ANDROID_SDK/chimpchat.jar"
ANDROID_JARS="$ANDROID_JARS:$ANDROID_SDK/ddmlib.jar"
ANDROID_JARS="$ANDROID_JARS:$ANDROID_SDK/hierarchyviewer2.jar"


# clear the app data:
adb shell pm clear $NATIVEDRIVER_APP

# start the instrumentation
adb shell am instrument "$NATIVEDRIVER_APP/com.google.android.testing.nativedriver.server.ServerInstrumentation"

# port forward
adb forward tcp:54129 tcp:54129

java -cp "$NATIVEDRIVER_JAR:$RFW_JAR:$XALAN_JAR:$SIKULI_JAR:$SEEMONKEY_JAR:$ANDROID_JARS" \
      	-Dpython.path="$RFW_JAR/Lib:$NATIVEDRIVER_JAR:$RFW_LIBS:$RFW_LIBS/android.sikuli:$SIKULI_JAR/Lib:$SEEMONKEY_JAR/python:libs/python" \
	-Dandroid.sdk.dir="$HOME/Library/android-sdk-macosx" \
        -Dnativedriver.instrumentation="$NATIVEDRIVER_APP" \
        org.robotframework.RobotFramework \
        --outputdir=results \
	--loglevel=TRACE \
        --noncritical indev \
        --noncritical warn \
        --critical final \
	"$RFW_SUITE"
