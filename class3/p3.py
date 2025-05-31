from collections import namedtuple
list1=[2,3,6,4,8,9,12,10,24,6]
list2=[26,32,61,45,86,97,12,100,24,6]
print(list1)
print(list2)

list1.append(43)
list1.insert(0,1)
print(list1)

list2[1]=5
print(list2)

list2.remove(6)
print(list2)

list2.pop(7)
print(list2)




print( )
tuple1=(98,33,42,81)
print(tuple1)

tuple1=tuple1+(11,)
print(tuple1)



print( )
my_range = range(1, 6)

my_range = list(my_range)
print(my_range)
my_range.append(6)
print("append:", my_range)

my_range[2] = 10
print("update:", my_range)

my_range.pop(3)
print("pop:", my_range)



print( )
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)
my_dict['d'] = 4
print("add:", my_dict)

my_dict['b'] = 10
print("update:", my_dict)


print( ) #f string
name = "Reahoon"
age = 25
print(f"My name is {name} and I am {age} years old.")

