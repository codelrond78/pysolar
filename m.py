from time import time
import numpy as np
from unyt import km, m
from numba import jit

int_data = list(range(12*31*24))

#a = np.array([[1, 2], [3, 4.7]], dtype='float32')
#b = np.array([[0, 0], [1, 0]], dtype='float32')
#z = np.array([[0, 0], [0, 0]], dtype='float32')

a = np.array(int_data, dtype='float32')
b = np.array(int_data, dtype='float32')
z = np.array(int_data, dtype='float32')

@jit(nopython=True)
def g(i, j):
    return i + j*2 + 10000

t1 = time()
#for n in range(1000):
#    for i, j, k in np.nditer([a, b, z], op_flags=[['readonly'], ['readonly'], ['readwrite']]):
#        k[...] = g(i, j)
#t2 = time()

#print(1000*(t2-t1))
for i in range(1000):
    for n in range(12*31*24):        
        z[n] = a[n] + b[n]*2 + 10000

t2 = time()

print(1000*(t2-t1))
