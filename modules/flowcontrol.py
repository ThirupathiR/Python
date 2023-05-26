print("Introduction to Flow Control\n=========================")

print("Flow Control Operators > < >- <= != ==\nExmples\n==========================")

print(4>2)
print(4<2)
print(4>=2)
print(4<=2)
print(4!=2)
print(4==2)
print(2==2.0)
print("Hello" == "Hello")
print("Hello" == "hello")

print(1<2 and 3<4)
print(1<2 or 3>4)
print(not 2==2.0)

print("======================\nBeginning of IF")
if 2!=4:
    print (str(True))

vegetable=input("Enter a vegetable name")
if vegetable=="Tomato":
    print("You entered Tomato")
else:
    print("You didn't entered Tomato")

print("Loan app\n===================")
gpa=float(input("Enter GPA - Grade Pont Average"))
inst_app=input("Is Student going to study at an approved institution")

if gpa>=3.7:
    if inst_app=="yes":
        print("The application qualifies for the loan")
    else:
        print("The application doesn't qualify since the institution is not approved")
else:
    print("The application doesn't qualify since the GPA is less than 3.7")

