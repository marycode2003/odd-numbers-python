#take a list of numbers from the user and print only the odd numbers.
numbers=[]
count=0
while count<100:
    n=input("please Enter a number(type a non-number to quit):")

    try:
       numbers.append(int(n))
       count+= 1
    except ValueError:
        print("exiting....")
        break
print("numbers:",numbers)
odd=[]
for num in numbers:
    if num % 2 != 0:
        odd.append(num)
#using list comprehension
odd=[num for num in numbers if num % 2 != 0]
print("odd numbers:",odd)
