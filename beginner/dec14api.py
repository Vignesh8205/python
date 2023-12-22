import json
import requests



# pip3 install requests


# link validation
# log in 
# menu in available 
# billing
# payments
# # payment 

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

#billing 
def billin(your_order,quantity):
    dhosa=30
    biriyani=100
    chicken_rice=80
    chicken_noodles=90
    if your_order=="dhosa":
        total=dhosa*quantity
        print(f"your total bill is {total}")
        payment(total)
    elif your_order=="biriyani":
         total=biriyani*quantity
         print(f"your total bill is {total}")
         payment(total)
    elif your_order=="chicken rice":
         total=chicken_rice*quantity
         print(f"your total bill is {total}")
         payment(total)
    elif your_order=="chicken noodels":
         total=chicken_noodles*quantity
         print(f"your total bill is {total}")
         payment(total)


# avilable menu
def available_food():
    menu=["dhosa","biriyani","chicken rice","chicken noodels"]
    print(f"********{menu}**********")
    your_order=input("enter your order:")
    if your_order in menu:
        print(f"{your_order} is available")
        quantity=int(input(f"how many {your_order}"))
        billin(your_order,quantity)

    else:
        print("your order is not avilable")


#2 login
def login(username,password):
    db_username="vignesh"
    db_password="6381748857"
    if db_username==username and db_password==password:
        print("login succes")
        available_food()
    else:
        print("invalid password or username")


# 1 link validation

def link_validation(status_code,data):
        
    if status_code==200:
        client_name=data["username"]
        client_pswd=data["passsword"]
        login(client_name,client_pswd)
        # login(data["username"],data["password"])
    else:
        print("invalid link")


# net work checking
api_url="https://demo8822566.mockable.io/vicky"
response=requests.get(api_url)

# link_validation(response.status_code,data)
data=response.json()
link_validation(response.status_code,data)
    
    






