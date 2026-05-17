# cd ~/cs50learning
# git add .
# git commit -m "what you did today"
# git push





#   revising a calculator

a=int(input("Enter your first Number :"))
b=int(input("Enter your second Number :"))

add=a+b
subtract=a-b
product=a*b
if b==0:
   division=None
else:
      division=a/b

c = input("Enter your Operator('+ - * / '): ")
if c == "+":           # compare string to string
    print(add)
elif c == "-":
    print(subtract)
elif c == "*":
    print(product)
elif c == "/":
    if b==0:
      print("Not Divisible")
    else :
            print(division)
else:
    print(f"{c} not recognized!")