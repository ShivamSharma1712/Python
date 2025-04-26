# we cannot use array without using libraries like numpy in python
list1 = [20, 25.5, 'hello'];
print(list1);
print(list1[2]);
print(list1[-1]);
list1[0]=15; # it is mutable we can insert value easily 
print(list1[0]);
#print(list1(-n));

list2 = [[10,'shivam'], [50.5,'sharma']];
print(list2[1]);
print(list2[0]);

#List Operations:
# 1.Concatenation
print(list1 + list2);

#Repeatation:
print(list1*5);

# Membership:
#in or not in
print('hello' in list1);
print([10,'shivam'] in list2); #returns true if u mention entire list elements
print([10] in list2 ) # returns false as u dont mention entire list elements

#Slicing:
#Syntax: list[start:end:step]
print(list1[::1])# print by jumping/skiping by 1 
print(list1[::-1])# reverse, print by jumping/skiping by -1
#print(list1[-1:0])# prints empty list, it doesnt find end point
print(list1[:]); # print entire list
print(list1[2:]); # print list from index 2
print(list1[:4]); # print list 0 to 4
print(list1[1:4]); # print list 1 to 4
print(list1[-6:-2]); #it starts index from last
print(list1[1::2]); # prints from index 1 and jumps 2


print(list1[::-1]); #print reverse of list, '::'it omits start & end
print(list1[:-1]); #it omits start i.e it by default starts with first 
#index and leaves the end element which is at -1 index

#list functions:

list3 = [225, 99.5, 'python'];
#1. len:
print(len(list3))

# 2. list(), empty the existing list
list3 = list();
print(list3) #empty the list3
str1 = 'aeiou';
list3= list(str1); #insert new elements in list3
print(list3)

# 3. append(): # insert at end of list
list3.append('shivam');
print(list3);
#we can also append list inside list
list3.append([100,200])
print(list3, '\n')

# 4. extend(): here insert elements of list3 in list1
list1.extend(list3)
print(list1)

# 5. insert(): insert elements at at specific position/index
list3.insert(2,25)
print(list3)

# 6. count(): count how many times an element is found 
list3.count(25)

# 7 index: # returns first index of an element, if not in list it returns error
list3.index(25) 
print(list3)

# 8. remove(): only first occurence of element is removed, 
# if not found generste error
list3.remove(25) # for removing no.
x = 'a'
list3.remove(x) #for removing string
print(list3, '\n') 

# 9. pop():
z = list3.pop(1)
print(z)
print(list3)

# 10. reverse():
list3.reverse();
print(list3);

''' 11. sort():
list3.sort();
print(list3); ''' 

# 12. sorted(), min(), max(), sum()















































