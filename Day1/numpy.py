l = range(10)

import numpy as np

a = np.arange(10)

b = np.arange(1,10,2)

c = np.linspace(0,1,6)

# linear space means we are dividing 0,1 in 6 equal spaces . 

a = np.ones((3,3))

b = np.zeros((3,3))

c = np.eye(3,2)

np.diag([1,2,3,4])

np.random.rand(4)

a = np.arange(10)

a[1:8:2]

a[5:] =10

b = a[::2]
a[5:] = b[::-1]

# if we change a b also auto change 
np.shares_memory(a,b)

b[0] = 7


c = np.random.randint(0,20,15)

c[[0,1]] = -2


'''
== used to compare 2 arrays 
> used to compare elements in array 
axis = 0 means col 1 means row

argmin used to find index of min ele in array 

vice versa 

armax

also functions like any all 

ravel convert 2d to 1d array

reshape to another shape 

resize used to resize array .
suppose 4 sieze array resize 8 then remaining values will be 0 . 

'''




