import numpy as np

# #0-D array:
# x=np.array(50)

# #1-D array using list
# a= np.array([1,2,3,4,5])

# #1-D array using tuple
# b= np.array((3,4,5))

# ##2-D array using list
# c= np.array([[1,2,3], [4,5,6], [3,4,5]])

# #3-D array using list
# d= np.array([[[1,2,3], [4,5,6]],[[7,8,9], [10,11,12]]] )
# print(x)
# print(a)
# print(b)
# print(c)
# print(d)

##another way of creating array
# e = [8,7,6,5,4]
# arr = np.array(e)
# print(arr)

# #array size from users:
# f=[]
# n=int(input('enter size of array'))

# for i in range(n):
#     val = int(input(f'enter value in array{[i]}:'))
#     f.append(val)
# print(f)

#FUNCTIONS OF ARRAY:
# # 1. finding dimension of arrays using ndim:
# print(a.ndim)
# print(c.ndim)
# print(d.ndim)
# print(arr.ndim)
    
# # 2. shape:
# g= [[1,2,3], [2,3,4], [4,5,6]]
# arr2=np.array(g)
# print('Shape of array is:', arr2.shape)

# # 3. zeros
# ar=np.zeros(2) # 1 dimensional array (dimension and then no. of values), # here we can give values without any tuple/list
# print(ar) 
# arr3=np.zeros([2,3]) # 2 dimensional array using list (dimension and then no. of values)
# print(arr3)

# # 4. ones
# arr4=np.ones((2,3)) # 2 dimensional array using tuple (dimension and then no. of values)
# print(arr4)

# # 5. eye
arr5= np.eye(4,4) # here we only have to give values without any tuple/list
print(arr5)

# # 6. diag
# arr6=np.diag([4,5,6,8]) # here we only have to give values within list
# print(arr6)
# #6.2 np.diag()
# print(np.diag(arr6)) # it gives diagonal element from array

# # 7. random.randint()
# arr7=np.random.randint(1,10,3) # gives random no. from np.random.randint(1, t0 9(n-1), 3 numbers)
# print(arr7)

# # 8. random.rand()
# arr7=np.random.rand(20) # gives ranom value b/w 0 to 1
# print(arr7)
# ar7=np.random.rand(2,3) # gives ranom value b/w 0 to 1,  we can also create 2d array
# print(ar7)

# #INDEXING AND SLICING IN 1 D ARRAY:
# j=[] #declare an array
# size = int(input('enter size of array'))

# for i in range(size):
#     val = int(input(f'enter value at index {i}'))
#     j.append(val)
# arr8=np.array(j)
# for i in range(arr8.size):
#     print(arr[i])