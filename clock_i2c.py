from ics import Calendar
from urllib2 import urlopen
import requests
import RPi.GPIO as GPIO
import time, sys
from RPLCD import CharLCD
from datetime import datetime
import lcddriver

def writeString(line, text):
	global USEI2C
	if USEI2C:
		lcd.lcd_display_string(text, (line+1))
	else:
		lcd.cursor_pos = (line, 0)
		lcd.write_string(text)

def checkCalendar():
	global row2
	url="https://calendar.google.com/calendar/ical/en-gb.indian%23holiday%40group.v.calendar.google.com/public/basic.ics"
	c = Calendar(requests.get(url).text)
	now = datetime.now()
	for e in c.events:
		if now.date() == e.begin.date():
			if len(e.name) > 16:
				row2.append(e.name[0:15])
			else:
				row2.append(e.name)
			print e.name + " / " + str(e.begin)

def updateSecondLine():
	global row2
	global row2Idx
	x = datetime.now()
	if x.second % 15 == 0:
		if row2Idx == (len(row2)-1):
			row2Idx=0
		else:
			row2Idx=row2Idx+1

row2=["Sydney"]
row2Idx=0
row2Txt=""
USEI2C=True
CLOCK_FORMAT_12H=True

GPIO.setmode(GPIO.BOARD)
if USEI2C:
	lcd = lcddriver.lcd()
else:
	lcd=CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=7, pin_e=12, pins_data=[32, 36, 38, 40])

lcdstr=""
lcdstr2=row2[0]
writeString(1, lcdstr2)
currentDay=0  #if changed, will be used to recheck calendar

while True:
	now = datetime.now()
	if now.day != currentDay:
		currentDay = now.day
		del row2[:]
		row2.append("Sydney")
		row2.append(now.strftime("%A"))
		checkCalendar()
	updateSecondLine()
	if CLOCK_FORMAT_12H:
		tmpstr=now.strftime("%d %b %I:%M %p")
	else:
		tmpstr=now.strftime("%d%b%Y %H:%M")
	if lcdstr != tmpstr:
		lcdstr = tmpstr
		writeString(0, lcdstr)
	if row2Txt != row2[row2Idx]:
		row2Txt = row2[row2Idx]
		writeString(1, '{:16}'.format(row2Txt))
	time.sleep(1)
writeString(0, "Bye!!!")
GPIO.cleanup()
sys.exit()
