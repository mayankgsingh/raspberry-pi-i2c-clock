#!/bin/bash
count=`ps -ef | grep clock_i2c | grep -v grep | wc -l`
if [ $count -gt 0 ]; then
	echo "program is running"
else
	echo "Command is not running"
	python /home/pi/scripts/python/clock_i2c.py&
fi
