# # # # #                 # Loops

# # # # # # print("meow\nmeow\nmeow")


# # # # # # if we want to print or do someting repetitive tasks like printing something 100 or more or many times its not logical to use prints statement that many times right ?

# # # # # # a loop is a block of code which does something again and again and again as stated under the parameters
# # # # # # "while" is way to start a loop

# # # # # # i=10
# # # # # # while i !=0:
# # # # # #     print("You are Gay")  #itll print "ur gay"until the logic hits the 0 
# # # # # #     i=i-1

# # # # # lets make a while loop which prints from 1-10
# # # # # i=1
# # # # # while i <=5:
# # # # #     print("hello")
# # # # #     i=i+1



# # # # for i in range(2):
# # # #     print("Meow")

# # # #using while loop to ask user to enter a number between 1-10
# # # num=int(input("Enter your Number: "))
# # # while num<=0 or num>=10:
# # #     print(f"{num} is not a valid Number")
# # #     num=int(input("Enter another Number: "))
# # # # else:
# # # #     print("Good boy!")



    
# # # for i in reversed(range(0,11,2)):  # to count backward youll need a reversed range function as used in that segment of code ! also if you want to count in difference of 2 then use third comma like(0,10,2)
# # #     print(i)
# # # print("nice u have contiued learning for range!")


# # # # to skip over a iteration u can use  a"continue" fucntion which is not exclusive to for only i.e it can be used in while loops too

# # # for i in range(15):
# # #     if i==13: #this determines if i is equals to 13 then .. and next line code says what to do after | probably that's waht i think how it works
# # #         continue   #this skips 13 and continue printing numbers
# # #     else:
# # #         print(i)


# # # # there is a "break"function too which just completely breaks the loop after specific conditions 

# # # for i in range(15):
# # #     if i==13: #this determines if i is equals to 13 then .. and next line code says what to do after | probably that's waht i think how it works
# # #         break   #this just breaks the loop after the loop reaches 13
# # #     else:
# # #         print(i)


# # #timer thingy using time library watchiing bro code also for loop too 

# # import time    # demo of how time module kinda works cuz its first time i used a module or library idk what to call it lol
# # time.sleep(3)
# # print("times up")


# # #now making an actual timer without sounds
# # import time
# # number=int(input("Enter timer's time: "))
# # for i in range(0,number):
# #     time.sleep(1)
# # print("Time's Up! ⏰")



# import time
# seconds = int(input("Enter timer time: "))
# for i in range(seconds, 0, -1):  # counts DOWN
#     print(i)
#     time.sleep(1)

# print("Time's Up! ⏰")


#making a programme where a user states number we print its product table till 10
num=int(input("Enter your Number: "))

for i in range(0,11):
    a=int(num*i)
    print(f"{num} x {i} = {a}")
    
   