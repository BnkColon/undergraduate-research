#!/usr/bin/env python

# Research Investigation : Spring 2015-2016
# Techniques for Anomaly Detection using Benford's Law
# 
# Using the data provided by NAB (https://github.com/numenta/NAB)
# we will analize the Benford's Law. 
#
import math
from sys import argv

def significantNumber(num): #recieve 0.0024
	number = num.split('.') # '0' '0024'
	aDot = number[1] # '0024'
	for d in range(0,len(aDot)):
		if aDot[d] != '0':
			return aDot[d]
		else:
			pass

def howManyNumbers(listCounter):
	allNum = [] # List to put all the numbers
	diNum = [] * 10  # List to put counts of numbers
	
	for i in range(0, len(listCounter)):
		allNum.append(int(listCounter[i])) # Change strings for numbers

	totalNum = len(allNum) 	# Total of numbers
	for c in range(1,10):
		diNum.insert(c, 1.0 * allNum.count(c)/totalNum)

	return diNum

def benford(listCounter):
	allNum = [] # List to put all the numbers
	diNum = [] * 10  # List to put counts of numbers
	for i in range(0, len(listCounter)):
		allNum.append(int(listCounter[i])) # Change strings for numbers
	for c in range(1,10):
		diNum.insert(c, allNum.count(c))
	return diNum

def rms(freq, expected):
    sum = 0
    for i in range(len(freq)):
        sum += (freq[i] - expected[i])**2
    return math.sqrt(sum)

## main 
if (len(argv) == 4):
	filename = argv[1]
	columnNumber = int(argv[2]) - 1
	windowSize = int(argv[3])

	with open(filename) as f:

		content = f.read().splitlines()	

	f.close()

	value = [] 		# For the values
	fDigit = [] 	# For the first significant digit

	# Take the only values of the line
	# 1.Starts in line 1 because line 0 contain column title. (range(1 ... )
	## timestamp,value,anomaly_score,raw_score,label,S(t)_reward_low_FP_rate,S(t)_reward_low_FN_rate,S(t)_standard

	# 2. The value is positioned in the second column. (.split(',')[1] ) columnNumber should be 1.
	## 2015-09-01 13:45:00,3.06,0.0301029996659,1.0,0,0.0,0.0,0.0
	for i in range(1,len(content)): # 1.
		if float(content[i].split(',')[columnNumber]) != int(0):
			value.append(content[i].split(',')[columnNumber]) # 2.
		else:
			pass

	# To that values, just select the first significant digit
	for j in range(0,len(value)):
		if value[j].isdigit() == True: 	# For int values
			if value[j][0].isdigit() == True:
				fDigit.append(value[j][0])
			else:
				print "Alert Anomaly: value = %d" % (value[j])
		else:  							# For float values
			if value[j].split('.')[0] != '0' : 	# Save the left dot number for a number like 12.003
				fDigit.append(value[j].split('.')[0][0]) # From 12.003 only save the 1
			else:								# Save the right dot number for a number like 0.0034
				fDigit.append(significantNumber(value[j]))

	# Remove 'None' values from the list
	#try:
	#	for r in range(0, fDigit.count(None)):
	#		fDigit.remove(None)

	#except ValueError:
	#	pass

	#print type(fDigit)
	#print len(fDigit)
	#values = howManyNumbers(fDigit)
	
	expected = [ math.log(1.0/d+1.0,10) for d in range(1,10)]
	
	### ONLY BENFORD GRAPH 
	#bVal =  benford(fDigit)
	#for n in range(0,len(bVal)):
	#	print n+1, bVal[n], expected[n]
	###
	
	
	for i in range(len(fDigit) - windowSize):
		valuesFD = howManyNumbers(fDigit[i:i+windowSize])
		print content[i].split(',')[0], rms(valuesFD,expected)
		# The timestamp is in the first column, that's why content[i].split(',')[0]

else: 
	print ""
	print "Need to provide the name of the file that have the data"
	print "and in what column is the value data"
	print "Example:"
	print "timestamp,value,anomaly_score,raw_score,label,S(t)_reward_low_FP_rate"
	print "The value column is the second"
	print ""
	print "Format to write the missing information"
	print "$ python benford-NAB.py fileName columnNumber"
	print "$ python benford-NAB.py numenta_occupancy_6005.csv 2"
	print ""


