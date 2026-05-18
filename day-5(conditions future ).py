# making a def function to check odd and even numbers
# def odd_even():
#     a=int(input("Enter your number: "))
#     if a%2==0:
#         print("The Number is Even")
#     else:
#         print("the Number is ODD")

# odd_even()


#making the same above program but using boolean , and other complicated things cuz my life isnt that hard that i need to complicate it furture
# def main():
#     a=int(input("Enter Your Number: "))
#     if is_even(a):
#         print("The Number is Even")
#     else:
#         print("The Number is ODD")

# def is_even(n):
#     return True if n%2==0 else False
# main()


#usiing match statement to make a programme to assign homes to hogwarts character 

name=input("Enter your Name: ")
match name :
    case "harry" |"hermonie"|"ron":
        print("gryffindor")
    case"draco":
        print("slytherin")
    case _:
        print("who?")