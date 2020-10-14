import numpy as np
import sys

#define a function that returns a value
def expo(x):	#x is an argument to the function
	return np.exp(x)	#return the e^x function

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i))) #call the expo function


#define a main function
def main():
	n = 10 # provide a default calue for n

	# check if there is a command line arg
	if(len(sys.argv)>1):
		n = int(sys.argv[1]) #if additional arg provvided, set n = arg

	#print e^x n times
	show_expo(n)

#run the main function
if __name__ == "__main__":
	main()
