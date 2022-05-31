import numpy as np
from unyt import km, m
from time import time
from numba import jit

M1 = 100000

int_data = list(range(12*31*24))
a = np.array(int_data, dtype='float32')*km
b = np.array(int_data, dtype='float32')*m
a_ = np.array(int_data, dtype='float32')
b_ = np.array(int_data, dtype='float32')

@jit(nopython=True)
def fast():
    a + b*3

@jit(nopython=True)
def fast2():
    a_ + b_*3


print("empezamos")
t0 = time()

for i in range(M1):
    fast()

t1 = time()

for i in range(M1):
    fast2()

t2 = time()

print("fin")
print(1*(t1 - t0))
print(1*(t2 - t1))
