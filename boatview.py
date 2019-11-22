#!/usr/bin/python -u

from dronekit import connect, Command, LocationGlobal
from pymavlink import mavutil
import time, sys, argparse, math
from datetime import datetime

address = '0.0.0.0'
port = 14552

#vehicle = connect('udpout:'+address+':'+str(port),wait_ready=False)
vehicle = connect('udpin:'+address+':'+str(port),wait_ready=False)


#connection_string = 'udp:localhost:14551'
#vehicle = connect(connection_string, wait_ready=True)

fileName = "boat.js"

while True:
	time.sleep(5)
	try:
		print(str(vehicle.location.global_frame.lat) , " " , str(vehicle.location.global_frame.lon))
		now = datetime.now()
		with open(fileName, "w") as f:
			f.write("var lat = " + str(vehicle.location.global_frame.lat) + ";\n")
			f.write("var lon = " + str(vehicle.location.global_frame.lon) + ";\n")
			f.write("var bat = " + str(vehicle.battery.voltage) + ";\n")
			f.write("var gps = " + str(vehicle.gps_0.satellites_visible) + ";\n")
			boatSpeed = ('{0:3.1f}'.format(vehicle.groundspeed))
			print(str(boatSpeed))
			f.write("var speed = " + str(boatSpeed) + ";\n")
			f.write("var t = \'" + now.strftime("%m/%d/%Y %H:%M:%S") + "\';\n")
	except:
		print("pass")
		pass
