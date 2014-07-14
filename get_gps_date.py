#!/usr/bin/env python

import serial

def main():
	ser = serial.Serial('/dev/ttyACM0', 9600)

	linecount = 0
	while True:

		line = ser.readline()
		linecount += 1
		splitStr = line.split(',')
		if len(splitStr) > 1:
			if splitStr[0] == '$GPRMC':
				wholetime = int(float(splitStr[1]))
				seconds = wholetime % 100
				minutes = (wholetime / 100) % 100
				hours = wholetime / 10000

				wholedate = int(splitStr[9])
				year = wholedate % 100
				month = (wholedate / 100) % 100
				day = wholedate / 10000

				print('20{:02d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(year, month, day, hours, minutes, seconds))
				break
		if linecount > 100:
			#give up after 100 sentences read
			break

if __name__ == '__main__':
	main()
