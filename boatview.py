import sys
from dronekit import connect

address = '0.0.0.0'
port = 14551

vehicle = connect('udpout:'+address+':'+str(port),wait_ready=False)

while True:
	print(str(vehicle.location.global_frame.lat))
