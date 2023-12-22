print("*****VICKY RESTAUERENT********")
print("*****menus=> 1.dhosa 2. biriyani 3. barota 4.chicken rice")
one_dhosa=30
one_biriyani=100
one_barota=12
one_chicken_rice=80

you_order=input("Enter your order:")
menus=["dhosa","biriyani","barota","chicken rice"]

if you_order in menus:
    print(f"your order {you_order} is available")
    if you_order=="dhosa":
         quantity=int(input(f"How many {you_order}:"))
         total=one_dhosa*quantity
         print(f"your total bill is {total}")
         if total>=1000:
              offer=total-200
              print(f"***diwali offer 200 less => you pay only {offer}")
    if you_order=="biriyani":
         quantity=int(input(f"How many {you_order}:"))
         total=one_biriyani*quantity
         print(f"your total bill is {total}")
         if total>=1000:
              offer=total-200
              print(f"***diwali offer 200 less => you pay only {offer}")
else:
     print("your food not available")

