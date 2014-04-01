from datetime import datetime
from math import sqrt


def datetime_interpretation(data):
	now = datetime.now()
	difference = (now - data).total_seconds()

	minute = 60
	hour = 60 * minute
	day = 24 * hour
	month = 31 * day
	year = 365 * day

	if difference <= 10:
		return "just now."
	elif difference < minute:
		return "%s seconds ago." % difference
	elif difference < hour:
		return "%s minutes ago." % int(difference/minute)
	elif difference < day:
		return "%s hours ago." % int(difference/hour)
	elif difference < month:
		return "%s days ago." % int(difference/day)
	elif difference < year:
		return "%s months ago." % int(difference/month)
	else:
		return "%s years ago." % int(difference/year)


def order_by_post(l):
	new_list = sorted(l, key=lambda k: k["posts"], reverse=True)
	for i in range(len(new_list)):
		if new_list[i]["posts"] == 0:
			new_list.pop(i)
	return new_list


def standard_deviation(l):
	avg = sum(l)/(len(l))
	print avg
	new_list = []
	for number in l:
		thing = float(number-avg)**2
		new_list.append(thing)
	print new_list
	avg2 = sum(new_list)/(len(new_list))
	print avg2
	return sqrt(float(avg2))


def get_stats(l):
	values = []
	stats = {}
	for user in l:
		values.append(user["posts"])
	values.sort()
	stats["average"] = sum(values)/len(values)
	stats["min"] = values[0]
	stats["max"] = values[-1]
	stats["standard deviation"] = standard_deviation(values)
	if len(values) % 2 != 0:
		stats["median"] = values[len(values)/2]
	else:
		index1 = len(values)/2
		index2 = len(values)/2 -1
		stats["median"] = (values[index1]+values[index2])/2
	return stats
