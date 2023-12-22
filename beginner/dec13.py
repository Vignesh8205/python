# module 
# what is modules 
# module its a code library
# a file containing set of function yo want include in your application
# two type of modules
# 1 default modules
# 2 library moduele
# 
# 
# 1 library module example
# system actual time module python module
import datetime
x=datetime.datetime.now()
print(x)


# intermediate 

# new   topic  python exception handling
#    handling errors

# 1 try block:
    #   to test a actual code
#
# 2 except: 
#    try block thrown an any error  . the except block will handle the error
# finally:
#    regardless result

# example
# try:
#     x=10
#     print(y)
# except:
#     print("this is system error")
# finally:
#     print("always iam running")



#   ****file handling ******
# 1 create the file =>x
# 2 read and view the file =>r
# 3 update the file 
# 4 delete the file
# 

# create the file 
# f=open("vicky.txt","x") # x is predifined
# print("file created")


#  read file
# f=open("vicky.txt","r") # r is predefined
# print(f.read())

# update file 
# f=open("vicky.txt","a") # a is pre defined #b w is overwrited
# print(f.write("good nit"))
# print("word added")

# delete
import os
os.remove("vicky.txt")
print("delted success")





