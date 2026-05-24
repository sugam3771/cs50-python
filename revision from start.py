# # # def greet(name): # "name" is a parameterr , also a empty box 
# # #     print("hello ",name)
# # # greet("sugam")
# # # greet("susan")


# # # def add(a, b):
# # #     return a + b        # SENDS value back

# # # result = add(1, 6)      # result = 8
# # # print(result)           # 8


# # # def greet(name="world"):
# # #     print("Hello ", name)
    
# # # greet()
# # # greet("sugam")


# # # def add(a, b):
# # #     return a + b
# # # result = add(3, 5)
# # # print(result)           

# # i=1
# # for i in (reversed(range(1,6))):
# #     print(i)
  
  
# # for i in (reversed(range(3))):
# # #     print("meow")


# # students = ["harry", "ron", "hermonie"]
# # # students[0]          # "harry" — indexing starts at 0
# # print(students[0])
# # # print(len(students))

# # students = ["harry", "ron", "hermonie"]
# # # for student in students:
# # #     print(student)



# # for i in range(len(students)):
# #     print(i+1, students[i])


# #directory


# # houses = {
# #     "harry": "gryffindor",
# #     "draco": "slytherin"
# # }

# # for i in houses:
# #     print(i,houses[i])





# # students = [
# #     {"name": "Harry",    "house": "Gryffindor"},
# #     {"name": "Draco",    "house": "Slytherin"},
# #     {"name": "Sugam",    "house": "Damak"},
# # ]

# # for i in students:
# #     print(i["name"],i["house"],sep=", ")



# # while True:
# #     try:
# #          x=int(input("Whats x? "))
# #          print(f"x is {x}")
# #          break
# #     except ValueError:
# #          print("thats not a integer")

# #     else:
# #         print("invalid operation")





# #asks for a name and age and prints hello name and age

# # name=input("what's your name? ")
# # age=int(input("what's your age ? "))
# # print(f"Hi {name}, you are {age} years old")

# #2 asks for 2 number and prints sum,diff,product and division
# # num1=int(input("What's first number? "))
# # num2=int(input("What's second number? "))
# # add=num1+num2
# # subtract=num1-num2
# # product=num1*num2
# # divison=num1/num2

# # print(f"add: {add}\nsubtract: {subtract}\nproduct: {product}\ndivison: {divison}")


# #3.. Ask for a number, print if positive, negative, or zero
# # a=float(input("Enter a Number:"))
# # if a==0:
# #     print(f"{a} equals 0")
# # elif a>0:
# #     print(f"{a} is a positive number")
# # else:
# #     print(f"{a} is a negative number")


# # Ask for age, print: Child / Teenager / Adult / Senior
# # age=int(input(" what's your age? "))
# # if age<0:
# #     print("invalid age ")
# #     age=int(input("what's your age?"))

# # elif age>0 and age<=9:
# #     print("you are a child")
# # elif age>8 and age<=   18:
# #     print("You are a teenager")
# # elif age>=18 and age<65:
# #     print("You are a adult")
# # else :
# #     print("you are a senior citizen")



# #  Ask for a number repeatedly until user enters positive number (use try/except for non-numbers too)
# while True:
#     try:
#         number=int(input("Enter a Number: "))
#         if number>0:
#             print(f"{number} is positive")
#             break
#         if number <=0:
#             print(f"{number} is not a valid Number")

#     except ValueError:
#         print(f"{number} is not a Number")


# 8. Print multiplication table for any number user enters

# number=int(input("Enter a Number: "))
# for i in range(1,11):
#     print(f"{number} X {i} = {number*i}")



#9. Make a simple login — username: "sugam", password: "1234" — 3 attempts only

for attempt in range(3):
    username=input("Enter Username: ")
    password=input("Enter Password: ")
    if username !="sugam" and password != "1234":
        print("Invalid Username or Password ")
    elif username=="sugam" and password=="1234":
        print("Valid Username and Password \nLogging in...")
        break
    
    else:
        remaining=2-attempt
        if remaining>0:
            print(f"Wrong! {remaining} attempt left..")
        else:
            print("Account locked")