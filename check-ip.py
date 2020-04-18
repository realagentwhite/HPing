import os, sys
from time import sleep
import subprocess

def check(address):
	try:
		with open(os.devnull, "wb") as limbo:
			ip=address
			result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
			stdout=limbo, stderr=limbo).wait()
			if result != 0:
				print(ip, "is NOT active")
			#else:
			#	print(ip, "is active")
	except Exception as e:
		print("An error ocurred: ")
		print(error)

address = input("Enter the IP/host you want to check: ")
#verify = input("Are you sure you want to check %s ? (Y/n) " % str(address)).lower()
#if verify != 'y':
#	sys.exit()

rest = int(input("How long do you want to wait until the next check? (between 0 and 60) "))
if rest < 0 or rest > 60:
	print("Enter a number between 0 and 60")
	sys.exit()
#if len(rest) == 0:
#	rest = 30

repeat = int(input("How many times would you like to check? (between 4 and 1000, default is 200) "))
x = 0

if repeat < 4 or repeat > 1000:
	print("You entered %s which is not a valid input" % str(repeat))
	print("Try again and use a number between 4 and 1000")
	sys.exit()
elif repeat >= 4 and repeat <= 1000:
	print("\nYou will not see any results until the host or IP entered stops responding.")
	for i in range(0,repeat+1):
		x += 1
		if x == repeat:
			print("Done checking.\nRun the script again to check another host/ip")
			sys.exit()
		else:
			check(address)
			sleep(rest)
else:
	repeat = 200
	x = 0
	print("\nYou will not see any results until the host or IP entered stops responding.")
	for i in range(0,repeat):
		x += 1
		if x == repeat:
			print("Done checking.\nRun the script again to check another host/ip")
			sys.exit()
		else:
			check(address)
			sleep(rest)
