import sys
import time

start_time = time.time()

def error():
	print "Usage: gcdlcm.py <Input-File-Name>"
	sys.exit(0)

#Euclid's algorithm
def gcd ( n1, n2 ):
	if ( n1 % n2 == 0):
		return n2
	else:
		return gcd ( n2, (n1 % n2))


def gcdlcm ( str ):
	line = str.split()
	n1 = int(line[0])
	n2 = int(line[1])
	if (n1 < n2 ):
		n1 = n1 ^ n2
		n2 = n1 ^ n2
		n1 = n1 ^ n2
	#n1 > n2
	if ( n2 == 0 or n1 == 0 ):
		print "Zero can't be an input for GCD and LCM calculation!"
		error()
		
	gcd_n1_n2 = gcd(n1, n2)
	lcm_n1_n2 = (n1 * n2) / gcd_n1_n2
	print ("%s %s" % (gcd_n1_n2, lcm_n1_n2))

########################
#    Main Function     #
########################
if (len(sys.argv) != 2):
	error()

#Read first line for number of test cases
array = []

with open (sys.argv[1], "r") as file:
	for line in file:
		array.append(line)
file.close()

testCase = array[0]

print ("File name - %s, Test case number - %s" % (sys.argv[1], testCase))

for str in array[1:]:
	gcdlcm ( str )

print("Execution time -  %s seconds" % (time.time() - start_time))
