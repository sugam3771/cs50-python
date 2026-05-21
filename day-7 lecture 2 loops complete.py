# # # def main():
# # #     while True:
# # #         a=input("Enter a Name: ")
# # #         n=int(input("What's n?"))
# # #         if n>0:
# # #             break
# # #     for _ in range(n):
# # #         print(f"Hello {a}")

# # # meow()

# # # def get_number:
# # #     a=int(input("Enter a Number: "))
# # #     return a






# # def main():
# #     number=get_number()
# #     meow(number)





# # def meow(n):
# #     for _ in range(n):
# #         print("Meow")
    


# # def get_number():
# #     while True:   #this defines a function that takes user input and returns it to 
# #         n=int(input("Enter a Number: "))
# #         if n>0:
# #             return n
    
        

# # main()




#                             # Lists

#         #making a lists of studensts of hogwarts
    

# # students=["harry" , "hermonie" , "ron"] 

# # print(students[0])#it calls specific value inside of a variable
# # print(students[1])
# # print(students[2])

# # for students in students:   #for loops can iterate over strings too
# #     print(students)

# # for i in range(len(students)):
# #     print(i+1 ,students[i])



# """
# ------------    # Dict   -----------------
# """
# # dict is ajust a collection of values that allows to associate with each other named by keys with values 

# # students=["harry" , "hermonie" , "ron", "draco"] 
# # houses=["gryffindor","gryffindor","gryffindor","slytherin"]


# # students={
# #     "hermonie":"gryffindor",
# #     "harry":"gryffindor",
# #     "ron":"gryffindor",
# #     "draco":"slytherine",
# #     "sugam":"damak",
# #     }

# # print(students["hermonie"])
# # print(students["ron"])
# # print(students["harry"])
# # print(students["draco"])
# # for student in students:
# #     print(student,students[student],sep=", ")



# # students=[
# #     {"name":"Hermonie","house":"Gryffindor","patronous":"Otter"},
# #     {"name":"Harry","house":"Gryffindor","patronous":"Stag"},
# #     {"name":"Ron","house":"Gryffindor","patronous":"Jack Russell terrier"},
# #     {"name":"Hraco","house":"Slyterin","patronous": None}  #none represents nonvalue or literally none which represent no value literally not any programme fault
    
# # ]

# # for student in students:
# #     print(student['name'],student["house"],student["patronous"],sep=", ")



# # def mario_game():
# #     number=get_number()
# #     hello(number) #only name is hello it prints other stuffs


# # def get_number():
# #     while True:
# #         number1=int(input("Enter a Number: "))
# #         if number1>0:
# #             return number1

# # def hello(number1):
# #     for _ in range(number1):
# #         print("#")

# # mario_game()





# def main():   #vertical 
#     print_column(4)       


# def print_column(n):
#     for _ in range(n):
#         print("?")
 

# main()



def main(): #horizontal
    print_row(4)

def print_row(breadth):
    print("?"*breadth)#   nahhh wtf how wtfff he jst did that like wtff lol


main()




# def main(): #horizontal and vertical both
#     print_square(3)

# def print_square(size):
#     for i in range(size):
#         print("#"*size)

# main()