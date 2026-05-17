                #pound to kilo or kilogram to pounds converter
a = int(input("1 for kg to pound | 2 for pound to kg: "))
b=float(input("Enter your Values: "))
if a==1:
   reasult=b*2.04623
   print(f"{b}Kg = {reasult:.2f}pounds")
elif a==2:
    reasult=b/2.04623
    print(f"{b}Pound = {reasult:.2f}Kg")

else:
    print("Invalid Option")


