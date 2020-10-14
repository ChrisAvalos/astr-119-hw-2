#python exceptions let you deal with unexpected results


try:
	print(a)	#this will throw an exception
except:
	print("a is not defined")


#there are specific errors in python to help with cases

try:
	print(a)	#this will throw a NameError
except NameError:
	print("a is still not defined")
except:
	print("something else went wrong!")

#This will break our program since a not defined
print(a)

