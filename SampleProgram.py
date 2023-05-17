
def SayHello(name):
    print ("Hello ", name)

def SayBye(name):
    print("Bye ", name)

SayHello("Sandhya")
SayBye("Sandhya")
print("Below initializaing two variables nub1, num2 and displaying the sum of those 2 numbers")
num1=10;
num2=15
sum=num1+num2;
print("Sum of", num1, "and", num2 , "is", sum)

print("Below initializaing two variables nub1, num2 and displaying the sum of those 2 numbers")
num3=25;
num4=15
diff=num3-num4;
print("Difference of of", num3, "and", num4 , "is", sum)

print( " 10 times 15 is ", 10 * 5)

print (" 120 is ", (120/10), " times 12")

print("I defined a custom method at the top and calling it below to Say Hello!")

SayHello("Thirupathi")
SayBye("Thirupathi")


# Function to do insertion sort
def insertionSort(arr):
    if (n := len(arr)) <= 1:
        return
    for i in range(1, n):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print("while i", i, " sorting", arr)


#sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
print("before sorting", arr)
insertionSort(arr)
print("after sorting", arr)
