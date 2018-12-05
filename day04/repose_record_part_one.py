#!/usr/bin/python
from datetime import datetime


def sleepiest_guard(records):
	datetime_a = None
	datetime_b = None

	guard_sleep_records = {}
	on_shift_guard_id = -1
	for record in records:
		timestamp = record.split('[')[1].split(']')[0]
		action = record.split(']')[1]
		#print action
		if 'begins shift' in action:

			on_shift_guard_id = action.split(' ')[2].split('#')[1]
		
			if on_shift_guard_id not in guard_sleep_records:
				print "Setting guard " + on_shift_guard_id + " to 0 minutes"
				guard_sleep_records[on_shift_guard_id] = 0


		elif 'falls asleep' in action:
			datetime_a = datetime.strptime(timestamp, '%Y-%m-%d %H:%M') # start of shift
		elif 'wakes up' in action:
			datetime_b = datetime.strptime(timestamp, '%Y-%m-%d %H:%M') # start of shift
			delta = datetime_b - datetime_a
			print "Adding " + str(delta.seconds/60) + " minutes to " + on_shift_guard_id + " guard"
			guard_sleep_records[on_shift_guard_id] += delta.seconds/60

	
	most_sleep = -1
	sleepiest_guard = -1
	#for guard, minutes_slept in guard_sleep_records():
	for guard, minutes_slept in guard_sleep_records.iteritems():
		print "guard " + guard + " slept " + str(minutes_slept) + " minutes"
		if minutes_slept > most_sleep:
			most_sleep = minutes_slept
			sleepiest_guard = guard

	print guard + " is the sleepiest guard, sleeping " + str(most_sleep) + " minutes"


fh = open('testinput.txt', 'r')

#records = fh.readlines().sort()
records = fh.readlines()
records.sort()

sleepiest_guard(records)
