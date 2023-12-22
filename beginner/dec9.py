# 5 membership operator 
# namm theduea value iruka illa ya nu check pandrathu
# in => vale iruku
# not in => value illa 

array=["apple","banana"]
print("apple" in array)
print("apple1" not in  array)

# 6 bitwise operator
# and => &
# or => |
# not => 

# identity operator 
# is 
# is not
thala="ajith"
valimai_hero=thala
print(thala is valimai_hero)
print(thala is not valimai_hero)


# user input 

# firstname=input("enter your first name: ")
# lastname=input("enter your last name: ")
# print(firstname,lastname)

# python data types
# 1 text type  =>strimg
# 2 integer or numerica => int,float
# 3 sequence => -list ,tuples
# 4 set 
# 5 mapping  =>the king of concept
# 6 boolean
# 7 none 

# 1 string 
# string are collection of charaacter paranded single quotes or 
# double quotes or trible quotes
#  

name="guna"
print(type(name))

#    string array
# collection of character

str="chennai"
# index value using 
print(str[2])

# string slicing
# syntax [startindex:endindex]
print(str[2:6])
# start index
print(str[4:])
# end index
print(str[:7])

# string methods

# upper case methods
na="kPmar"
print(na.upper())

print(na.lower())

# list | tuples | set | dict
# 1 list 
fruits=["apple","banana","carrot","kiwi","banana"] # list allows duplicate values
fruits[1]="watermelon" # it allow value changeble

print(fruits)
print(type(fruits))

# tuple
fruits1=("apple","banana","carrot","kiwi","banana")
fruits2=("dragon fruit") # it is consider string data becaause it one values


print(fruits1)
print(type(fruits1))


# set
fruits3={"apple","banana","carrot","kiwi","banana","apple"} # not allowed duplicate value
print(fruits3)
print(type(fruits3))

# dict
det={"name":"vicky","lastname":"sugumar","age":23}
det["age"]=40 # value is changeble  
print(det)
print(type(det))


# boolean type 
# true or false is boolean type

a=True
b=False
print(type(a))




# none type 
x=None #it is dummy value 

print(type(x))

# interview topic 
# type conversion 
# one type to another type changing is type conversion
list_tuple=tuple(fruits)
print(list_tuple)






