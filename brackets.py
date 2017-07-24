import sys
import time
import os.path

start_time = time.time()

def error():
	print "Incorrect usage!"
	print "Usage: brackets.py <Input-File-Name>"
	sys.exit(0)


def max ( n1, n2 ):
	if (n1 > n2):
		return n1
	else:
		return n2
	
# Algorithm:-
#	FUNCTION F( S - a valid parentheses sequence )
#	BEGIN
#		balance = 0
#		max_balance = 0
#		FOR index FROM 1 TO LENGTH(S)
#		BEGIN
#			if S[index] == '(' then balance = balance + 1
#			if S[index] == ')' then balance = balance - 1
#			max_balance = max( max_balance, balance )
#		END
#		RETURN max_balance
#	END

def bracket_Algorithm ( str ):
	balance = 0
	max_balance = 0
	index = 0
	for index in range (0, len(str)):
		if (str[index] == "("):
			balance = balance + 1
		if (str[index] == ")"):
			balance = balance - 1
		max_balance = max (max_balance, balance)
	
	return max_balance


def bracket ( str ):
	balance = bracket_Algorithm (str)
	
	result = ""
	index = 0
	
	while (index < balance):
		result = "(" + result + ")"
		index = index + 1
	
	print result
	
	
	
########################
#    Main Function     #
########################
if (len(sys.argv) != 2):
	error()

#Read first line for number of test cases
if (!os.path.exists(sys.argv[1])):
	error()

array = []
with open (sys.argv[1], "r") as file:
	for line in file:
		array.append(line)
file.close()

testCase = array[0]

print ("File name - %s, Test case number - %s" % (sys.argv[1], testCase))

for str in array[1:]:
	bracket ( str )

print("Execution time -  %s seconds" % (time.time() - start_time))
