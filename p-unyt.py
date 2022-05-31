import numpy as np
from unyt import km
from time import time

int_data = list(range(1000000))
float32_data = np.array(int_data, dtype='float32')*km
float32_data2 = np.array(int_data, dtype='float32')

t0 = time()

for i in range(1000):
    np.sum(float32_data)

t1 = time()

for i in range(1000):
    np.sum(float32_data2)

t2 = time()

print(1000*(t1 - t0))
print(1000*(t2 - t1))
