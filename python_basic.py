#print hello world 
print("hello hi") #string
print('hello') # string


""" these will give error
print("print("hi")")
print('print('Python')') """

# thers no issue if we apply semicolon or not
print("print('hi')");
print('print("Python")');

# using \n
print("hello\n hi\n python")

#concat strings:
print("hello" + "python") #concat without space
print("hello" + " python")#concat with space
print("hello" +  " " + "python")#concat with space
#  print("hello" + " python") # indentation error as u give space before print()

#input():
# use of two input simultaneously displays you only 1 output
''' input("what is your name")
print("hello" + input("what is your name")) '''

# to use multiple input() simultaneously use variables
fname= input("what is your fname")
lname = input("what is your lname")
print("hello", fname, lname)  

length = len(fname) # it takes only one parameter
print(length)
#print(len(1234))  it gives error as int as no length
print(len("1234")) #but string has length

# Swap two numbers using 3 variables:
a = 5;
b = 10;
c = a;
a = b;
b = c;
print(a,b,c)
# Swap 2 nos using 2 variables:
d = 10;
e = 20;
d = d+10;
e = e-10;
print("d=", d, "e=", e) #without concatenation
#print("d=" +d) concationation is only for string not for int values 
print(d, e)
print("d=", d)
print("e=", e)

print(type(d))
f = 123456789123456789123456789123456789123456789123456789123456789
print(f)
g= 0b1010 #binary prefix
h = 0o123 #octal prefix
i = 0x15e #hexadecimal prefix
j= "shivam"
print(g,h,i)
print(j[0]) #printing string
print("shivam\'s  \\n \"sharma\"")

lenth = len("shivam")
print("your name has " + str(lenth) + " characters") #typecasting
print("your name has", lenth, "characters\n\n")

#typecasting:
'''print('invalid typecasting')
k = "shiv"
print(int(k)) invalid typecasting
print(float(k)) invalid typecasting'''

print('valid typecasting')
l = 12
m= 15.5455
print(float(l)) # valid typecasting
print(int(m),'\n\n') # valid typecasting

# Sum of two numbers:
print('sum of two numbers')
num1=int(input("enter num1"))
num2=int(input("enter num2"))
print( num1 + num2)
sum = num1 + num2 # valid typecasting of string to int
print(sum)































