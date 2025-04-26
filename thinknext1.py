#tuples immmutable
a = (1,2,3,'shivam')
print(a)
print(a[1]) 
print(id(a))
b,c,d,e =5,6,7,'hello'
f = b,c,d,e;
print(f)
print(list(f)) # typecasting
#concatenation occurs only b/w same datatype

# swap first and third element
A = ['preet', 'anvi', 'sunil', 'heena'] 
A[0], A[2] = A[2],A[0]
print(A[0], A[2])

# replace value
A[1] = 'ansh'
print(A)

#insert value
A.insert(1,'shivam')
print(A)

# delete
del A[2]
print(A)


# min
print(min(A)) # h has small value then s and p

#max
print(max(A))

# Dictionary
y = {1: 'shivam', 2:'ansh', 5:'anish'}
print(y);
print(y.keys())
print(y.values())
print(y[2])
print(y.get(1)) # find value  using index no or key
w = list(y.keys()) # find index or key no using value 
q = list(y.values())

r = q.index('shivam')
print(w[r])
print(r) # not this way wrong way

#SET
s = {1,2,3,'shivam', True, 1} # not repeat values and true =1 & false = 0
print(s)

f = {}; #empty dictionary
print(type(f))

g = set() # empty set
print(type(g))






















                                                             