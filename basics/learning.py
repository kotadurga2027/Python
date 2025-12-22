print("hello world")
# this is kota durga - this is single line comment

"""i am learning python 
here i am practicing
python basics""" # this multi line commands or docstrings.


#variables
a = 10 #integern 
x,y = 10,20
b = 20.5  #float value
c = "durga" # string
d = True


print(a, type(a))
print(b,type(b))
print(c,type(c))
print(x,y)


# data types :
#Numeric type: int,float,complex(a+bj) a is real part b is imaginary parth and j represents imaginary part
#sequence type - string , list,tuple
# mapping type - dict
#set types - set, frozenset
# boolean type - bool
#binary type - bytes,bytery

#sequence type: 
#string - immutable
name = "My name is kota durga gangumalla"
print(type(name))
print(name[2])
print(name[5])
print(name[-1])

#list type: mutable
a = [] # this is empty list
b = list()
a = ['kota','durga',27,1997,64.8]
print(a[0])
print(a[3])
print(a[-1])

print(len(a))

#tuple:immutable
b = ()
b = ('kota','durga',27)
print(b[1])
print(b[-1])

#boolean: 
a = True
b = False

print(type(a))

#set - mutable,unorders and remove the duplicates, it's not print the output in order wise.
a = set()
names = ["kota","durga","kota","sai","krishna","durga"]
greeting = " hi this is is kota hi durga"

print(set(names))
print(set(greeting))

#mapping data type: key value pair
#dictonary - dict
#{ key: value}
a = {} #empty dictonary
a = dict() # empty dictonary
b = { "name": "kota","age":27,1:"hello"}
# dict() is builtin function 
c = dict(name="kota",age=30, city="hyd")
print(a)
print(b)
print(c)
print("***************************")
print(b["name"])
print(b[1])
#print(b[2])
print(c.get("age"))


#input method - taking input from user or taking dynamic input
# name = input("enter your name:")
# #print(name)
# print(type(name))
# #age = int(input("enter your age:"))
# #print(age)
# print(type(age))

# age,date = input("enter the you age and date:").split(",")
# print(age,date)
# print(type(age), type(date))
# print(age+date)
# # print(sum(age,date)) it will show error, because it is not possible

# x,y = map(int, input("enter the values with comma:").split(","))
# print(x,y)
# print(type(x),type(y))
# print(x+y)
# print(sum([x,y]))

#strings formating

name = "kotadurga"
age = 27
print(f"My name is {name} and my age is {age}")
details = "my name is {0} and my age is {1}".format(name,age)
details1 = "my name is {} and my age is {}".format("raju",25)
details2 = "my age is {1} and my name is {0}".format(name,age)
print(details)
print(details1)
print(details2)
details_4 = f"my name is {name} and my age is {age}"
print(details)










    



