# test file for the eigenvalue animation
import numpy as np
import eigenAnimation as eigAn

# basic functionality test
np.random.seed(450)
n = 200
A = np.random.randn(n,n)
eigAn.animation(A)

# test range 
range = [-1,1,-1,10]
n = 200
B = np.random.randn(n,n)
eigAn.animation(A,Range=range)

# now test with gridview on
np.random.seed(450)
n = 7
A = np.random.randn(n,n)
eigAn.animation(A,grid_view=True)

# this test looks at small matrix perturbations of the identity
A = np.diag([4.0, 3.0, 2.0, 1.0])
A[0,1]=5
eigAn.animation(A,grid_view=True)