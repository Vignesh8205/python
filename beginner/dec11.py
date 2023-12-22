# conditional state ment
# 1 if
# 2 else
# 3 elif
# nested if

# if condition syntax

# if  condition:
# print statement 

# voting

# age=int(input("enter your age : "))
# if age>=18:
#     print("you can vote")
# else:
#     print("you can not vote")

# 

# it festival enter test

print("*******welcome to IT winter festivel*********")
print("****only allowed students note: BCA,MCA,MSC,BSC,CSE,IT*****")

# watchman asking question
department=input("enter your department:")
departments=["BCA","MCA","MSC","CSE","IT"]

if department in departments:
    print("welcome guys pls come inside")
    if "BCA"==department:
        print("hi BCA guys goto 1 floor")
        have_yoy_reg=input("have you register tell yes or no:")
        if have_yoy_reg=="yes":
            print("please come inside")
        else:
            print("please registered first")
    elif "MCA"==department:
        print(f"hi {department} guys goto 2 floor")
        have_yoy_reg=input("have you register tell yes or no:")
        if have_yoy_reg=="yes":
            print("please come inside")
        else:
            print("please registered first") 
    elif "BSC"==department:
        print("hi BSC guys goto 3 floor")
        have_yoy_reg=input("have you register tell yes or no:")
        if have_yoy_reg=="yes":
            print("please come inside")
        else:
            print("please registered first")             
    elif "CSE"==department:
        print("hi CSE guys goto 4 floor")
        have_yoy_reg=input("have you register tell yes or no:")
        if have_yoy_reg=="yes":
            print("please come inside")
        else:
            print("please registered first")    

elif department=="teacher":
    print("sorry mam goto 2 gate")
elif department=="thanni_can":
    print("plaease goto back side")
else:
    print("sorry you can't allowed")