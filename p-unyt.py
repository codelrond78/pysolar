import numpy as np
from unyt import km, m
from time import time

M1 = 10000

int_data = list(range(12*31*24))
a = np.array(int_data, dtype='float32')*km
b = np.array(int_data, dtype='float32')*m
a_ = np.array(int_data, dtype='float32')
b_ = np.array(int_data, dtype='float32')

print("empezamos")
t0 = time()

for i in range(M1):
    #np.sum(float32_data)
    a + b*3

t1 = time()

for i in range(M1):
    #np.sum(float32_data2)
    a_ + b_*3

t2 = time()

print("fin")
print(1*(t1 - t0))
print(1*(t2 - t1))
