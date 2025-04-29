"""
module 6 practice.py
by Paul Renaud
4/28/2025
IvyTech SDEV 220
"""

# Module 6 chapter 12 exercises
# These all involve datetime.

def ch12ex():
	# 12.1
	# write current date to a file
	from datetime import date
	today = date.today()

	print("Writing to file...", end="")
	with open("today.txt", "w") as f:
		f.write(str(today))
	print("Done.")
		

	# 12.2
	# read date from file as a string
	print("Reading from file...", end="")
	from datetime import datetime
	with open("today.txt") as f:
		today_str = f.readline()
	print("Done.")

		
	# 12.3
	# convert string to date format
	print("Converting string to date...", end="")
	today = datetime.strptime(today_str, "%Y-%m-%d")
	print(str(today.date()))
	print("Done.")

# 15.1
# Use multiprocessing to create three separate processes.
# Make each one wait a random number of seconds between zero and one, print the current time, and then exit.
import multiprocessing
import random
import time
from datetime import datetime

def wait_then_print():
	wait_time = random.random()
	time.sleep(wait_time)
	print(datetime.now())

def start_process():
	for n in range(3):
	    p = multiprocessing.Process(target=wait_then_print)
	    p.start()

if __name__ == "__main__":
	ch12ex()
	print("Running multiple processes...")
	start_process()
	time.sleep(2)
	print("Done.")

