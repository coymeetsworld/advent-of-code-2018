#!/usr/bin/python
from datetime import datetime

def find_sleepiest_minute_of_guards(records):
	guard_sleep_records = {}
	start_minute = -1
	end_minute = -1

	for record in records:
		timestamp = record.split('[')[1].split(']')[0]
		action = record.split(']')[1]
		if 'begins shift' in action:
			guard_id = action.split(' ')[2].split('#')[1]
			if guard_id not in guard_sleep_records:
				guard_sleep_records[guard_id] = {}
		elif 'falls asleep' in action:
			start_minute = int(timestamp.split(':')[1])
		elif 'wakes up' in action:
			end_minute = int(timestamp.split(':')[1])
			for minute in range(start_minute, end_minute):
				if minute not in guard_sleep_records[guard_id]:
					guard_sleep_records[guard_id][minute] = 1
				else:
					guard_sleep_records[guard_id][minute] += 1
			start_minute = -1
			end_minute = -1

	sleepy_guard_id = -1
	sleepy_minute = -1
	most_frequent_sleep_minute = -1
	for guard_id in guard_sleep_records:
		for minute in guard_sleep_records[guard_id]:
			if guard_sleep_records[guard_id][minute] > most_frequent_sleep_minute:
				most_frequent_sleep_minute = guard_sleep_records[guard_id][minute]
				sleepy_guard_id = guard_id
				sleepy_minute = minute

	return sleepy_guard_id, sleepy_minute


fh = open('input.txt', 'r')

#records = fh.readlines().sort()
records = fh.readlines()
fh.close()
records.sort()


guard_id, most_frequent_sleep_minute = find_sleepiest_minute_of_guards(records)
print "Guard " + str(guard_id) + " sleeps the same minute more than any guard, at minute " + str(most_frequent_sleep_minute)
print "Multiply them together: " + str(int(guard_id)*most_frequent_sleep_minute)

