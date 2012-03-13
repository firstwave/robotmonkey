#!/bin/sh

RFW_LIBS="examples/robot-libraries"
RFW_SUITE="examples/robot-suite"

RFW_JAR="libs/robotframework-2.6.3.jar"
SIKULI_JAR="libs/sikuli-script.jar"
SEEMONKEY_JAR="libs/seemonkey.jar"

ANDROID_SDK="/Users/obartley/Library/android-sdk-macosx/tools/lib"
ANDROID_JARS="$ANDROID_SDK/guavalib.jar"
ANDROID_JARS="$ANDROID_JARS:$ANDROID_SDK/monkeyrunner.jar"
ANDROID_JARS="$ANDROID_JARS:$ANDROID_SDK/sdklib.jar"
ANDROID_JARS="$ANDROID_JARS:$ANDROID_SDK/chimpchat.jar"
ANDROID_JARS="$ANDROID_JARS:$ANDROID_SDK/ddmlib.jar"
ANDROID_JARS="$ANDROID_JARS:$ANDROID_SDK/hierarchyviewer2.jar"

java -cp "$RFW_JAR:$SIKULI_JAR:$SEEMONKEY_JAR:$ANDROID_JARS" \
	-Dpython.path="$RFW_JAR/Lib:$SIKULI_JAR/Lib:$SEEMONKEY_JAR/python:libs/python" \
	-Dandroid.sdk.dir="$HOME/Library/android-sdk-macosx" \
	org.robotframework.RobotFramework \
	--pythonpath="$RFW_LIBS/seemonkey/*" \
        --pythonpath="$RFW_LIBS/seemonkey/*/*" \
	--outputdir=results \
	--loglevel=TRACE \
        --noncritical indev \
        --noncritical warn \
        --critical final \
        --exclude indev \
        --listener listeners.withSnapshots \
        --listener listeners.withVerboseKeywords \
	"$RFW_SUITE"
