                #pound to kilo or kilogram to pounds converter
a=int(input("1 for kilo and 2 for pound to kilo: "))
b=float(input("Enter your Values: "))
if a==1:
    print(b*2.204623)
elif a==2:
    print(b/2.204623)
else:
    print("Values Undefined")

print