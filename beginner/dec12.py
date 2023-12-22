# looping state ment
# lopp is a repate some thing over and over particular condition satisfied 
# two loops in python
# 1 while loop
# 2 for loop

#  what is while loop
#    we can excute a set of statement as long as a condition is true
# syntax
# while condition:
        # print statement
        # increament
# i=0
# while i<5:
#     print(i)
#     i+=1 #i=i+1


# break state ment 
# 
# i=0
# while i<5:
#     print(i)
#     if i==3:
#         break # we can stop the current iteration
#     i+=1

# continue

# i=1
# while i<5:
#     i+=1
    
#     if i==3:
#         continue # we can skip the current iteration
#     print(i)

# for loop 
# iterateing over a sequence
#  for iterable_variable_name in declaration_variable_name:
#          print(iterable_variable_name)

# fruits=["apple","banana","mango","orange"]
# for i in fruits:
  
#     if i=="mango":
#         # break
#         continue
#     print(i)

    #   range in for loop
# for i in range()
 

# function
# function is a block of code whick only only runs when it called
# syntax
# def function_name():
#     print("hii guys")
# function_name() #calling the function

def python_boys():
    print("hii boys")
python_boys()

# argument passing to the function
def vicky(firstname,lastname):
    print(f"my firstname is {firstname}")
    print(f"my lastname is {lastname}")
vicky("vicky","sukumar")

# conditionanl statement using in calling the function

def goa():
    packge=10000
    print(f"goa package is {packge}  per person")
    var=input("do you want continue press yes")
    if var=="yes":
        main_function()
    else:
        print("thanks for visiting our app")
def ooty():
    packge=6000
    print(f"ooty package is {packge}  per person")
    var=input("do you want continue press yes")
    if var=="yes":
        main_function()
    else:
        print("thanks for visiting our app")



def main_function():
    print("type 1 => goa")
    print("type 2 => ooty")
    user=int(input("Enter your number: "))
    if user == 1:
        goa()
    elif user == 2:
        ooty()
    else:
        print("pls type 1 or type 2")

main_function()

 
 

