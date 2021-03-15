import serial
import time

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)
time.sleep(0.01)
while (True):
	data = arduino.read()
	if (not data):
		break
		

def write_read(x):
	#arduino.write(bytes("a", 'utf-8'))
	arduino.write(bytes(x, 'utf-8'))
	arduino.flush()
	time.sleep(0.02)
	data = arduino.read(arduino.inWaiting())
	return data
count=0
while count<=100:
	#num = input("Enter a number: ")
	num = count
	num = "A{:03d}".format(num)
	value = write_read(num)
	print(value)
	count+=1
	

