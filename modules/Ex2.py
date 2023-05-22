def name_printer(name):
    print(name)

def ex1():
    name = input("Enter name")
    name_printer(name)
def calculate_area(l,w,h):
    return l*w*h

def fahrenheit(cel):
    return (18 * cel + 320) / 10
    #return round((1.8 * cel + 32), 1)

def ex2():
    l = int(input("Enter Length of the Prism"))
    w = int(input("Enter width of the Prism"))
    h = int(input("Enter height of the Prism"))
    print("The volume of the rectangular prism is " + str(calculate_area(l, w, h))+ " cubic feet.")

def ex3():
    celsius = int(input("Please enter an integer value for degrees celsius. "))
    print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")

#ex1()
#ex2()
ex3()

