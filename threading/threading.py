#!/usr/bin/python3

import _thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 10:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create 4 threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 1, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 1, ) )
   _thread.start_new_thread( print_time, ("Thread-3", 1, ) )
   _thread.start_new_thread( print_time, ("Thread-4", 1, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass