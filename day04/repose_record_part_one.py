#!/usr/bin/python
from datetime import datetime


def find_sleepiest_guard(records):
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
				#print "Setting guard " + on_shift_guard_id + " to 0 minutes"
				guard_sleep_records[on_shift_guard_id] = 0


		elif 'falls asleep' in action:
			datetime_a = datetime.strptime(timestamp, '%Y-%m-%d %H:%M') # start of shift
		elif 'wakes up' in action:
			datetime_b = datetime.strptime(timestamp, '%Y-%m-%d %H:%M') # start of shift
			delta = datetime_b - datetime_a
			#print "Adding " + str(delta.seconds/60) + " minutes to " + on_shift_guard_id + " guard"
			guard_sleep_records[on_shift_guard_id] += delta.seconds/60

	
	most_sleep = -1
	sleepiest_guard = -1
	#for guard, minutes_slept in guard_sleep_records():
	for guard, minutes_slept in guard_sleep_records.iteritems():
		#print "guard " + guard + " slept " + str(minutes_slept) + " minutes"
		if minutes_slept > most_sleep:
			most_sleep = minutes_slept
			sleepiest_guard = guard

	return sleepiest_guard


def find_sleepiest_minute_of_guard(sleepiest_guard, records):
	guard_sleep_records = {}
	sleepiest_guard_on_shift = False
	start_minute = -1
	end_minute = -1

	for record in records:
		timestamp = record.split('[')[1].split(']')[0]
		action = record.split(']')[1]
		if 'begins shift' in action:
			guard_id = action.split(' ')[2].split('#')[1]
			if guard_id == sleepiest_guard:
				sleepiest_guard_on_shift = True
			else:
				sleepiest_guard_on_shift = False
		elif 'falls asleep' in action and sleepiest_guard_on_shift:
			start_minute = int(timestamp.split(':')[1])
			if start_minute not in guard_sleep_records:
				guard_sleep_records[start_minute] = 0
		elif 'wakes up' in action and sleepiest_guard_on_shift:
			end_minute = int(timestamp.split(':')[1])
			#print "from " + str(start_minute) + " to " + str(end_minute)
			for minute in range(start_minute, end_minute):
				if minute not in guard_sleep_records:
					guard_sleep_records[minute] = 1
				else:
					guard_sleep_records[minute] += 1
			start_minute = -1
			end_minute = -1


	
	most_frequent_minute_of_sleep = -1
	most_frequent = -1
	for minute, freq in guard_sleep_records.iteritems():
		if freq > most_frequent:
			most_frequent_minute_of_sleep = minute
			most_frequent = freq
		#print "minute " + str(minute) + " was slept + " + str(freq) + " times"

	#print "Most frequent minute is minute " + str(most_frequent_minute_of_sleep)
	return most_frequent_minute_of_sleep

					
	


fh = open('input.txt', 'r')

#records = fh.readlines().sort()
records = fh.readlines()
fh.close()
records.sort()

sleepiest_guard = find_sleepiest_guard(records)

sleepiest_minute_of_guard = find_sleepiest_minute_of_guard(sleepiest_guard, records)



print "Sleepiest guard: " + str(sleepiest_guard)
print "Minute # he sleeps the most frequent: " + str(sleepiest_minute_of_guard)
print "Enter " + str(int(sleepiest_guard)*sleepiest_minute_of_guard) + " (sleepiest_guard * minute chosen)"
