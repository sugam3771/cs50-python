# # #  == represents equuality symbol and only one "=" represents assignemnt symbol

# # # COMPARING VALUES AND CONDITIONS STARTS FROM LECTURE 1

# # # x=int((input("whats x?")))
# # # y=int(input("whats y?"))

# # # if x>y:
# # #     print("x is greater than y")    #it doesnt feels fater to use elif in short code but in longer programes it matters a lot

# # # elif x<y:
# # #     print("x is less than y ")

# # # elif x==y:
# # #     print("x equals to y")
    


# # #     #using ELSE 

# # # x=int(input("whqats x"))
# # # y=int(input("whats y?"))

# # # if x>y:
# # #     print("x is greater than y")

# # # if x<y:
# # #     print("x is less the y")

# # # else :
# # #     print("x is equals to y")





# # #   using or 

# # x=int(input("whqats x"))
# # y=int(input("whats y?"))


# # if x>y or x<y:
# #     print("x is not equal to y ")
# # else:
# #     print("x equals to y")


# #   MAKING CODE EVBN SIMPLE AND CLEANER

# x=int(input("whqats x"))
# y=int(input("whats y?"))


# if x !=y:     #using OPERATOR != which means not equal
#     print("x is not equal to y ")
# else:
#     print("x equals to y")




                   # he made a new file named grade.py


   # making a grade marking program

mark=int(input("State your Mark :"))
if mark>=90 and mark<101:
    print('Your Grade is A+')
elif mark>=80 and mark<90 :
    print("Your Grade is A")
elif mark>=70 and mark<80 :
    print("Your Grade is B+")
elif mark>=60 and mark<70:
    print("Your Grade is B ")
elif mark>=50 and mark<60:
    print("Your Grade is C+")
    if mark>=40 and mark<50:
        print("Your Grade is C ")
else :
    print("Ungradable ")
