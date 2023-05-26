counter=0
while(counter<3):
    print("Something " + str(counter))
    counter+=1

#counter=int(input("Enter Number"))
counter=25
sum=0
while(counter >=1):
   sum+=counter
   counter-=1
print("Sum of All numbers from 0 to your input is " + str(sum))


#name=input("Enter a String")
name="This is a sample String"
count=0
for char in name:
    count+=1

print("Number of characters in " + str(name) + " are " + str(count))

var_list=range(count)
for num in var_list:
    print(name[num])
end_val=count/2
var_list=range(0,count//2)
for num in var_list:
    print(name[num])

count=50
list_range=range(1,51)
for num in list_range:
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)

print("Factorial")
fact_val=1
count=int(input("Enter a number"))
for num in range(1,count+1):
    fact_val*=num
print("Factorial of count is " + str(fact_val))