# TASk  airport verification
# commander ticket cheking
# covid test => negative travel positive => you cant travel
# yvinigiration cheking reason in travel
# weight cheking 20 kammiya irukanum 20 kg adhigama iruntha weit korakanum 
#boardig checking all complete enjoy journey not complete you go checking

your_ticket_no=input("Enter your ticket no:")
booking_tickets=["12","22","45","54"]
count=0
if your_ticket_no in booking_tickets: # first ticket checking
    print(f"your ticket no is {your_ticket_no} verified succesfully")
    count+=1
    covid=input("your covid status positive or negative: ")
    if covid=="positive":  # covid test
        print("your patient goto hospital immediately")
    else:
        print("your allwed goto next process")
        what_reason=input("what reason in travel :")
        count+=1
        if what_reason=="tour" or what_reason=="work": # reason in travel test
            count+=1
            what_your_logege_weight=int(input("Enter your loggege weight :"))
            if what_your_logege_weight <=20:
             print("your accepted") # luggage weight test
             count+=1
            #  lugage weapon test
             lugage_product1=input("Tell me the luggage product 1:")
             lugage_product2=input("Tell me the luggage product 2:")
             lugage_product3=input("Tell me the luggage product 3:")
             not_permited_product=["pistel","knife","atomic_bomp"]
             if lugage_product1 in not_permited_product or  lugage_product2 in not_permited_product or lugage_product3 in not_permited_product:
                print("your under arrest ")
             else:
               print("your permited goto next process")
               count+=1
               final_test=input("are you ready travel any struggle yes or no:")
               if final_test=="no":
                  count+=1
                  print("Final test is completed  enjoy your journey ")
                #   configuration test
                  if count==6:
                     print("happy journey enjoy your life")
                  else:
                     print(f" 6 test must your test is  {count} please balnce test configuration")
               else:
                  print("ok you go home")
            else:
             print("please reduce the weight")
        else:
           print("only allowed tour or work ")
else:
    print("your not allowed ")