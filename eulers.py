# Implement a version of explicit Euler's method
import numpy as np
import scipy as sp
from scipy.optimize import root_scalar as rt


# the standard Euler's method is 
# y_(n+1) = y_n + h*f_(x_n,y_n) 

def feuler(f,x0,a,b,h):
    N = int(np.ceil((b-a)/h)) #get the apx number of points in the linspace and convert to int
    x = np.linspace(a,b,N)

    y = np.ones(len(x)) # initialize a vector for our solution
    y[0] = x0 # this is the IC
    ######## Euler's method implementation
    for k in range(0,len(x)-1):
        fval = f(x[k],y[k]) # get the function value at this point
        y[k+1]= y[k]+h*fval # update y value

    return y

# the backwards Euler method. Using rootfinding, computes
# y_k+1 = y_k + hf(x_k+1,y_k+1)

def beuler(f,x0,a,b,h):
    N = int(np.ceil((b-a)/h)) 
    x = np.linspace(a,b,N) # create the mesh pts

    y = np.zeros(len(x)) # init a solution vector
    y[0] = x0

    # implement backwards Euler's
    for k in range(0,len(x)-1):
        def fupdate(yguess):
            return yguess-y[k]-h*f(x[k+1],yguess)
        # get the soln as a fixed point
        y[k+1] = rt(fupdate,x0=y[k]).root
    
    return y

# Implementation of forward euler's to a system of ODEs. 
# Here, we assume that f is a function parameterized by parameter s
def sysfeuler(f,x0,a,b,s=0,h=1e-3):
    N = int(np.ceil((b-a)/h)) #get the apx number of points in the linspace and convert to int
    t = np.linspace(a,b,N) # create the time pts
    y = np.zeros((len(x0),N),dtype=float)
    
    for k in range(len(x0)):
        y[k][0] = x0[k] # initial condition
    
    # now iterate
    for m in range(N-1):
        for k in range(len(x0)):
            y[k][m+1] = y[k][m]+h*f(y[0][m],y[1][m],s)[k]

    return y


# TODO: find a suitable version of 2D backwards Euler. Generalizing it is tricky, 
# but it might be possible 