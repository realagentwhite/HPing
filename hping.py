#!/usr/bin/env python3

"""
HPing
Written by: Andrew (aka AgentWhite)
Twitter: @_agentwhite_
Website: https://thegibson.xyz
"""

version = "0.1.4"

import os, sys
from time import sleep
import subprocess

# python 3 compat
try: 
	input = raw_input
except NameError: 
	pass

# Give some color to the texts
class bcolors:
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	ENDC = '\033[0m'

def self_update():
	# force https for git
	#def git_https_force():
	#	subprocess.Popen('git config --global url."https://github.com/".insteadOf git@github.com:;git config --global url."https://".insteadOf git://', shell=True).wait()

	# force https
	#git_https_force()

	# try to update ourself first
	print("Trying to update myself first.. Then starting...")
	subprocess.Popen("git pull", shell=True).wait()


def banner():
	banner = bcolors.YELLOW + '''
ooooo ooooo oooooooooo  o88                           
 888   888   888    888 oooo  oo oooooo     oooooooo8 
 888ooo888   888oooo88   888   888   888  888    88o  
 888   888   888         888   888   888   888oo888o  
o888o o888o o888o       o888o o888o o888o 888     888 
                                           888ooo888                 
	''' + bcolors.ENDC
	banner += bcolors.BOLD + bcolors.RED + 'Version %s' % str(version)
	banner += '''
	HPing
	Written by: Andrew (aka AgentWhite)
	Twitter: @_agentwhite_
	Website: https://thegibson.xyz\n''' + bcolors.ENDC
	return banner

def check(address, get_alerts, count, repeat):
	try:
		with open(os.devnull, "wb") as limbo:
			ip=address
			result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
			stdout=limbo, stderr=limbo).wait()
			if result != 0:
				print("[" + bcolors.BOLD + bcolors.GREEN + str(count) + bcolors.ENDC + "/" + \
					bcolors.BOLD + bcolors.GREEN + str(repeat) + bcolors.ENDC + "] " + \
					bcolors.YELLOW + ip + bcolors.ENDC +bcolors.RED + bcolors.BOLD + " is not active"+ bcolors.ENDC)
			if result == 0 and get_alerts == True:
				print("[" + bcolors.BOLD + bcolors.GREEN + str(count) + bcolors.ENDC + "/" + \
				bcolors.BOLD + bcolors.GREEN + str(repeat) + bcolors.ENDC + "] " + bcolors.YELLOW \
				+ ip + bcolors.ENDC +bcolors.GREEN + bcolors.BOLD + " is active"+ bcolors.ENDC)
	except Exception as error:
		print("An error ocurred: ")
		print(error)
		input("Press enter to continue...")
		main()

def run_hping(address, get_alerts, repeat, rest):
	try:
		# Declare variables
		count = 0
		x = 0
		if get_alerts == False:
			print("\nYou will not see any results until the host or IP entered stops responding.")

		for i in range(0,repeat+1):
			x += 1
			count = x
			if count == repeat+1:
				print("Done checking.\nRun the script again to check another host/ip")
				sys.exit()
			else:
				check(address, get_alerts, count, repeat)
				sleep(rest)
	except KeyboardInterrupt:
		print("Caught ctrl+c\nExiting now...")
		sys.exit()
	except Exception as error:
		print("*"*20)
		print(error)
		print("*"*20)
		input("Press enter to continue...")
		main()


def main():
	try:
		os.system("clear")
		# Clear variables for when executing script again after exceptions
		address = ""
		rest = 0
		repeat = 0
		alerts = False
		
		if '-h' in sys.argv or '--help' in sys.argv:
			print("\nJust run the program either python2 or python3\nYou can also run it using ./hping.py\n")
			sys.exit()
		
		print(bcolors.YELLOW + bcolors.BOLD + banner() + bcolors.ENDC)
		address = input("Enter the IP/host you want to check: ")
		rest = input("How long do you want to wait until the next check? (default 4) ")
		if rest < '0' or rest > '60':
			print("Using default timeout as 4")
			rest = 4
		elif len(rest) <= 0:
			print("Using default timeout as 4")
			rest = 4
		
		repeat = input("How many times would you like to check? (greater than 4, default is 60) ")
		if repeat < '0':
			print("Using default to check every 60 seconds")
			repeat = 60
		elif len(repeat) == 0:
			print("Using default to check every 60 seconds")
			repeat = 60
			
		alerts = input("Would you like to get alert if the host/IP is responding to pings? (Y/n) ").lower()

		if alerts == 'y':
			get_alerts = True
		elif alerts == 'n':
			get_alerts = False
		else:
			get_alerts = True
		
		os.system("cls || clear")
		print(banner())
		repeat = int(repeat)
		rest = int(rest)
		
		run_hping(address, get_alerts, repeat, rest)

	except KeyboardInterrupt:
		print("Caught ctrl+c\nExiting now...")
		sys.exit()
	except Exception as error:
		print("*"*20)
		print(error)
		print("*"*20)

if __name__ == "__main__":
	if os.geteuid() != 0:
		print("\nWe autocheck for updates and need sudo permission since you most likely\ndownloaded me using PTF? IDK")
		print("This needs to be run as root. Please sudo it up! Exiting...")
		sys.exit()
	self_update()
	sleep(1)
	main()
else:
	sys.exit()
