# This is a python file! The '#' character indicates that the following line is a comment.

# The following is an example for how to define a function in Python
# def tells the compiler that hello_world is the name of a function
# this implementation of hello_world takes a string as an argument,
# which has default value of the empty string. If the user calls 
# hello_world() without an argument, then the compiler uses ''
# as the default value of the argument.
#Implement the Riemann Sum approximation for integrals.

import numpy as np

def func(x): #write here whatever function we want to integrate
    return np.sin(x)


def riemann(a,b,n): #implement right-biased riemann sum between endpoints a and b with n rectangles
    vfunc = np.vectorize(func)
    arr = np.linspace(a,b,n)
    dx = arr[1]-arr[0]
    rsum = sum(dx*vfunc(arr+dx)) #we add dx to all points to make it right-biased
    return rsum

