print("hai")
print("\n\n\n\nhai\t\t\t\t\thai\n\tjai\b\b\b\b\n\n\n\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")

#str="Thirupathi"
#print(str[1:4])


var1="Just do it!"
print(var1[10:])
print(var1[10])
sliceDo=var1[5:7]
print(sliceDo)
sliceJust=var1[0:4]
print(sliceJust)

slice1=var1[5:]
slice2="Don't"
finalStr=slice2+ " "+slice1
print(slice2, slice1)
print(finalStr)


varFloat=10.1
print(type(varFloat))
myType=type(varFloat)

print(str(varFloat) + " is a float.")


ex1=True
ex2=100
ex3=123.45
print(type(ex1))
print(type(ex2))
print(type(ex3))


ex4 = str(True)
ex5 = str(100)
ex6 = str(123.45)
print(ex4)
print(ex5)
print(ex6)
print(type(ex4))
print(type(ex5))
print(type(ex6))

#name = input("What is your name?")
#quest = input("What is your quest?")
#color = input("What is your favorite color?")

print("So your name is " + name + ", your quest is " + quest + ", and your favorite color is " + color + ".")


user_input = int(input("Enter an Integer"))
print(user_input+10)