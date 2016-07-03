'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a =  7, b = 13


0 1 1 1 
   +
1 1 0 1

1)
XOR = 1 0 1 0
CAR = 1 0 1 0 

2)
XOR = 0 0 0 0 0 
CAR = 1 0 1 0 0

3)
XOR  = 1 0 1 0 0 
CAR = 0





'''

	
def add_two_integers(a, b, depth):

	a = ctypes.c_int32(a).value
	b = ctypes.c_int32(b).value
	print(a,b)
	if b == 0:
		return a
	else:
		return add_two_integers(a^b,((a&b)<<1), depth+1)


import ctypes	
a = -1
b = 19	

print(add_two_integers(a, b, 0))


