# # # # # doing assgnments of loops - day 5 | 06:02 pm 

# # # # password=(input("Enter your Password: "))
# # # # while password !="sugam123":
# # # #     password=(input("Enter your correct  Password: "))   #idk why when i make a logic to accept right password it didnt work and cause some problem in else statement but when i did  !+ statement it worked right away
# # # # else:
# # # #     print("Access Granted.")




# # # # asking user to guess a numbber bwtween 1-10 which answer is 7 .keeps askking until ans is 7 and prints too high or too low 
# # # print("Guess A Number From 1-10")
# # # num=int(input("Enter your Number: "))

# # # while num==7:
# # #     print("Correct Answer !")
    
    
    
# # # while num>7:
# # #         print("Too High! ")
# # #         num=int(input("another guess!: "))
# # # while num<7:
# # #         print("Too Low! ")
# # #         num=int(input("another guess!: "))
    



# # #above guessign game is wrong and contains infinite loop and too messy belowis good version
# # # num=int(input("enter your number: "))

# # # while num !=7:
# # #     if num>7:
# # #         print("Too High!")
# # #         num=int(input("another guess !"))
# # #     else:
# # #         print("Too Low!")
# # #         num=int(input("another guess !"))


# # #printing num from 1-100 divisible by 3
# # # print("correct ans!")

# # # for i in range(1,100):
# # #     if i%3==0:
# # #         print(i)


# # #aks user for a number and prints its factorial
# # num=int(input("Enter a Number: "))
# # reasult=1
# # for i in reversed(range(1,num+1)):
# #     reasult=reasult*i
# # print(reasult)
    

# #the above program which taks number and pritns its factorial ..idk how it works properly so yeaaa. 

# #
# # for i in range(1,6):
# #     print(1)
# #     i==2
# #     while i=a:
# #         print(2)

# #the above program doesnt work and it turns out that i need nested loops or smth to do it so yeaa its for tomorrow 




# # a simple ATM program where 
# """
# starting balance=1000
# asks user:deposit,withdraw or balance
# keeps running until u type exit 
# dont allow withdrawing more than balance || this gotta be hell of a programma and ill call it a day from programming after or if i completed it lol
# """




# # a=input("Deposit , Withdraw , Balance , quit: ")
# # starting_balance=10000

# # if a== " deposit ":
# #     c =int(input("Enter Deposit Amount: "))
# #     print(f"{a} has been deposited in your account")
    
# balance = 10000

# while True:
#     print("\nChoose an option:")
#     print("deposit")
#     print("withdraw")
#     print("balance")
#     print("exit")

#     choice = input("Enter choice: ")

#     if choice == "deposit":
#         amount = int(input("Enter amount to deposit: "))
#         balance = balance + amount
#         print("New balance:", balance)

#     elif choice == "withdraw":
#         amount = int(input("Enter amount to withdraw: "))

#         if amount > balance:
#             print("Not enough balance!")

#         else:
#             balance = balance - amount
#             print("New balance:", balance)

#     elif choice == "balance":
#         print("Current balance:", balance)

#     elif choice == "exit":
#         print("Thank you for using ATM")
#         break

#     else:
#         print("Invalid choice")





balance = 10000

while True:
    print("\nChoose an option:")
    print("deposit")
    print("withdraw")
    print("balance")
    print("exit")

    choice = input("Enter choice: ")

    if choice == "deposit":
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("New balance:", balance)

    elif choice == "withdraw":
        amount = int(input("Enter amount to withdraw: "))

        if amount > balance:
            print("Not enough balance!")

        