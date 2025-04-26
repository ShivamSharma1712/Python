# operators, mutable and immutable, delete operation.
#Arithmetic Operators
# we can use PEMDAS (parantheses, exponent, ,mul, div, add, sub)
a = 20
b = 10
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b) #a/b provides float value as 
#answer but to get int value as answer we use floor division a//b

# if we take input from user then input value is always int then we
# have to use typecasting
'''num1=input("enter num1")
num2=input("enter num2")
print(num1 + num2) # it concatenates numbers as strings
print(int(num1) + int(num2))'''

# Logical Operators
print(a<=20 and b<=10)
print(a<20 or b==10)
print(not a) # every non zero is considered as 1 

# Bitwise Operators
c=5; d=4;
print(c & d) #bitwise and  
print(c|d) #bitwise or
print(c^d) #bitwise xor
print(~c) # bitwise not 1s complement of c 0101 - 1010 (-6 not 10)
print(c<<2) # bitwise left shift by 2(0101- 010100) left bits are not discarded
print(c>>2) # bitwise right shift by 2(0101 - 0001) right bits are discarded

# Identity Operator

#Variables are references (or pointers) to objects.
#The objects themselves occupy memory, but the variable
#names are references to these objects 
# two or more objects are pointing to the same memory location or not
# eg a=5 and b=5, both a and b are references pointing to memory location of 5
# In python we can reuse same objects having same data type
# but this only applies on -5 to 256 or for mostly used strings eg hello
# 'is not' is opposite of 'is' operator
e = 5; f=5
print(e is f)
print(id(e)) #it returns address of object on which a points
print(id(f)) #it returns address of object on which b points
print(id(5))

g = 257; h = 257; p= 257; 
print(g is h);
print(id(g)) #now you see they both points to different memory address
# as it exceeds 0 to 256 limit of integers
print(id(h))
print(id(257))

i= "hello"; j="hello";
print(i is j)
print(id(i))
print(id(j))
print(id("hello"))
# 'is not' is opposite of 'is' operator

#Membership operator: used to find elements
arr = [1,2,3,4,5];
print('\n'); # datatype is list not array

print(type(arr));
print(5 in arr);
print(10 in arr);
print(5 not in arr);
print(10 not in arr);

#Immutable: in mutable we cannot insert, ++/--, update on same object
#When we say that a data type is immutable, we mean that once an instance 
# of that type is created, its value cannot be changed. 

x = 10  # Create an integer object with value 10
print(id(x))  # Print the memory address of the object

x = 20  # Reassign the variable x to a new integer object with value 20
print(id(x))  # Print the memory address of the new object

# Mutable:
# in mutable we can insert, append, ++/--, update on same object
#This means that once an immutable datatype(array) is created, 
# its contents can be modified without creating a new array 

my_list = [1, 2, 3]
print(id(my_list))  # Memory address of the original list

my_list[0] = 10  # Modify the first element
print(my_list)  # [10, 2, 3]
print(id(my_list))  # Same memory address as the original list

my_list.append(4)  # Add a new element
print(my_list)  # [10, 2, 3, 4]
print(id(my_list))  # Same memory address as the original list

#Delete operation in python:
# delete is same for both mutable and immutable:
# if we delete the variable it deletes reference(variable name) to the the
#  object but doesnot directly deletes object, it first look for the other 
# reference for the object i.e object is pointed by some other variable or 
# not, if it is pointed by another variable then it doesnot allow garbage
#collection of object, but if no other variable points the object it allows 
# garbage collection for that object(i.e deletes the object).







































































