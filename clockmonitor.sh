#!/bin/bash

count=`ps -ef | grep clock_i2c | grep -v grep | wc -l`
if [ $count -gt 0 ]; then
	echo "program is running"
else
	echo "Command is not running"
	# Get current script path
	SCRIPT=$(readlink -f "$0")
	# get directory
	SCRIPTPATH=$(dirname "$SCRIPT")
	python $SCRIPTPATH/clock_i2c.py&
fi
