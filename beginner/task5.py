print("****welcome to xyz hotel roooms avilable******")

# login page
username="vignesh"
password="vicky2002"

def login():
    enter_user=input("Enter your user name:")
    enter_paswd=input("password:")
    if enter_user==username:
        if password==enter_paswd:
            print("login succes")
            mani_function()
        else:
            login()
            print("incorrect password")
    else:
        login()
        print("incorrect username")

# biiing functioon
def billing(day,food,rent):
    total=day*food+day*rent
    print(f"your total bill is {total}")
    payment(total)

# payment 

def payment(yourbill):
    payment_now=int(input("Enter cash amount :"))
    if yourbill==payment_now:
        print("payment sucess thanks   for visiting")
    elif yourbill<payment_now:
        balance=payment_now-yourbill
        print(f"please take your balnce {balance} thanks for visiting")
    else:
        low_cost=yourbill-payment_now
        print(f"you cost is less please give full payment balnce cost is {low_cost}")

# manin function
# room booking 
def mani_function():
    already_booking_rooms=[1,2,3,4,5,6,7,9,11,15,19,13]
    avilable_limit=20
    print(f"****already booking rooms {already_booking_rooms}***")
    selct_room_no=int(input("Enter your lucky room No:"))
    if selct_room_no not in already_booking_rooms and  selct_room_no<=avilable_limit:
        print("your room is available ")
        per_day=1000
        day_limit=10
        per_day_food=250
        enter_living_day=int(input("how many day living :"))
        billing(enter_living_day,per_day_food,per_day)

    else:
        mani_function()
        print("this room  is already booked ")
    
# 1 st calling function 
login()
