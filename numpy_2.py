import numpy as np

#INDEXING AND SLICING IN 1 D ARRAY:
j=[] #declare an array
size = int(input('enter size of array'))

for i in range(size):
    val = int(input(f'enter value at index {[i]}'))
    j.append(val)
    arr8=np.array(j)
for i in range(arr8.size):
    print(arr8[i])


# 








