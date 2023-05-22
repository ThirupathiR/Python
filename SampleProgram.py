import modules.operations as myOps

myOps.SayHello("Sandhya")
myOps.SayBye("Sandhya")
print("Below initializaing two variables nub1, num2 and displaying the sum of those 2 numbers")
num1 = 10;
num2 = 15
sum = num1 + num2;
print("Sum of", num1, "and", num2 , "is", sum)

print("Below initializaing two variables nub1, num2 and displaying the sum of those 2 numbers")
num3=25;
num4=15
diff=num3-num4;
print("Difference of of", num3, "and", num4 , "is", sum)

print( " 10 times 15 is ", 10 * 5)

print (" 120 is ", (120/10), " times 12")

print("I defined a custom method at the top and calling it below to Say Hello!")


# Function to do insertion sort



#sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
print("before sorting", arr)
myOps.insertionSort(arr)
print("after sorting", arr)
