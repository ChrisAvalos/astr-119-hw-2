import numpy as np 		#import numpy library

#integers
i = 10 			#integer
print("The type of i is ",type(i))	#print out the type

a_i = np.zeros(i,dtype=int)	#an array of ints
print("The type of a_i is ",type(a_i))	#print out the type
print("The type of a_i[0] is ",type(a_i[0]))	#print out the type


#floats
x = 119.0 #floating point number
print("the type of x is ",type(x))	#print out the type

y = 1.19e2 #sci not float
print("The type of y is ",type(y)) 	#print out the type


z = np.zeros(i,dtype=float)	#declare an array of floats
print("The type of z is ",type(z))	#print out the type
print("The type of z[0] is ",type(z[0]))	#print out the type

 