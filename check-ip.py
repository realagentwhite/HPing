import os, sys
from time import sleep
import subprocess

# Give some color to the texts
class bcolors:
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	ENDC = '\033[0m'



def banner():
	pipinger = '''
 888888ba  oo  888888ba  oo                                     
 88    `8b     88    `8b                                        
a88aaaa8P' dP a88aaaa8P' dP 88d888b. .d8888b. .d8888b. 88d888b. 
 88        88  88        88 88'  `88 88'  `88 88ooood8 88'  `88 
 88        88  88        88 88    88 88.  .88 88.  ... 88       
 dP        dP  dP        dP dP    dP `8888P88 `88888P' dP       
oooooooooooooooooooooooooooooooooooooo~~~~.88~oooooooooooooooooo
                                      d8888P                    
	'''
	return pipinger

def check(address, get_alerts):
	try:
		with open(os.devnull, "wb") as limbo:
			ip=address
			result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
			stdout=limbo, stderr=limbo).wait()
			if result != 0:
				print(ip + bcolors.RED + bcolors.BOLD + " is not active"+ bcolors.ENDC)
			if result == 0 and get_alerts == True:
				print(ip + bcolors.GREEN + bcolors.BOLD + " is active"+ bcolors.ENDC)
	except Exception as error:
		print("An error ocurred: ")
		print(error)
		input("Press enter to continue...")
		main()

def main():
	try:
		os.system("clear")
		print(bcolors.YELLOW + bcolors.BOLD + banner() + bcolors.ENDC)
		address = input("Enter the IP/host you want to check: ")
		rest = int(input("How long do you want to wait until the next check? (between 0 and 60) "))
		if rest < 0 or rest > 60:
			print("Enter a number between 0 and 60")
			sys.exit()

		repeat = int(input("How many times would you like to check? (greater than 4, default is 200) "))
		x = 0
		
		alerts = input("Would you like to get alert if the host/IP is responding to pings? (Y/n) ").lower()
		if alerts == 'y':
			get_alerts = True
		else:
			get_alerts = False
		
		if repeat < 4:
			print("You entered %s which is not a valid input" % str(repeat))
			print("Try again and use a number between 4 and 1000")
			sys.exit()
		elif repeat >= 4 and repeat <= 1000:
			if get_alerts == False:
				print("\nYou will not see any results until the host or IP entered stops responding.")

			for i in range(0,repeat+1):
				x += 1
				if x == repeat+1:
					print("Done checking.\nRun the script again to check another host/ip")
				else:
					check(address, get_alerts)
					sleep(rest)
		else:
			repeat = 200
			x = 0
			if get_alerts == False:
				print("\nYou will not see any results until the host or IP entered stops responding.")

			for i in range(0,repeat+1):
				x += 1
				if x == repeat:
					print("Done checking.\nRun the script again to check another host/ip")
				else:
					check(address, get_alerts)
					sleep(rest)

	except KeyboardInterrupt:
		print("Caught ctrl+c\nExiting now...")
		sys.exit()
	except Exception as error:
		print("*"*20)
		print(error)
		print("*"*20)

main()
