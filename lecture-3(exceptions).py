# # # print("hello world")  #unterminated means not closed or started smth but not completed which means not terminated{unterminated}



# # #promkpt thje user for integer and prints it

# # # x=int(input("what is x: "))
# # # print(f"x is {x}")# is a user enters a string itll be a error 



# # #try and except
# # #scope refers to a block of code where a variable exits
# # # try:
# # #     x=int(input("what is x: "))
# # #     print(f"x is {x}")# is a user enters a string itll be a error 
# # # except ValueError:  #if there is a value error it print the below code as a defense
# # #     print("x is not a integer")
    
# # while True:
# #     try:
# #         x=int(input("Whats x? "))
# #     except ValueError:
# #         print(f"X is not an integer")
        
# #     else:  
# #         break
# # print(f"x is {x}") 
   





# # # while True:
# # #     try:
# # #         x=int(input("Whats x? "))
# # #         break
# # #     except ValueError:
# # #         print(f"X is not an integer")
        
    
# # # print(f"x is {x}") 
   

# def main():
#     x=get_int()
#     print(f" x is {x}")





# def get_int():
#     while True:
#         try:
#             x=int(input("Whats x? "))
#         except ValueError:
#             print("X is not an integer")
        
#         else:  
#             break # can also directly do return x and itll be the same
#     return x

# main()





# def main():
#     x=get_int()
#     print(f" x is {x}")


# def get_int():
#     while True:
#         try:
#             return int(input("Whats x? "))
#         except ValueError:
#             pass
# main()






def main():
    x=get_int("enter age: ")
    print(f"age is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()