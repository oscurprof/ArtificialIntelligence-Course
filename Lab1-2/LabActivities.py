# Activity 1
print("Activity 1")
print(24)
print(4.2)
print(234)
print(45.90)

# Activity 2
print("Activity 2")
print('''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Agent47"''')

# Activity 3
print("Activity 3")
print(2 + 2)
print(50 - 4)
print(23.5 - 2.0)
print(23 - 18.5)
print(5 * 6)
print(2.5 * 10)
print(2.5 * 2.5)
print(28 / 4)
print(26 / 4)

#Activity 4
print("Activity 4")
print(28 // 4)      
print(26 // 4)      
print(int(26 / 4))  
print(int(28 / 4))  
print(28 % 4)        
print(26 % 4)     

#Activity 5
print("Activity 5")
print(4 ** 3)
print(4 ** 10)
print(4 ** 29)
print(4 ** 150)
print(4 ** 1000)

#Activity 6
print("Activity 6")
print(2 + 3 * 6)                       
print((2 + 3) * 6)                     
print(48565878 * 578453)               
print(2 + 2)                           
print((5 - 1) * ((7 + 1) / (3 - 1)))   
print(5 + 7.42 + 5)  

#Activity 7
print("Activity 7")
name = input('What is your name? ')
print('Hello ' + name)

job = input('What is your job? ')
print('Your job is ' + job)

num = input('Give me a number? ')
print('You said: ' + str(num))

#Activity 8
print("Activity 8")
n = input("Enter a number ")
if int(n) % 2 == 0:
    print("The given number is an even number")

#Activity 9
print("Activity 9")
n = input("Enter a number ")
if int(n) % 2 == 0:
    print("The given number is an even number")
else:
    print("The given number is an odd number")

#Activity 10
print("Activity 10")
summation = 0
i = 1
while i <= 10:
    summation = summation + i
    i = i + 1
print("sum is ", summation)

#Activity 11
print("Activity 11")
summ = 0
i = 0
while i <= 4:
    s = input("enter a number")
    n = int(s)
    summ = summ + n
    i = i + 1
print("sum is ", summ)

#Activity 12
print("Activity 12")
sum = 0
s = input("Enter an integer value...")
n = int(s)
while n != 0:
    sum = sum + n
    s = input("Enter an integer value...")
    n = int(s)
print("Sum of given values is ", sum)

#Activity 13
print("Activity 13")
isPrime = True
i = 2
n = int(input("enter a number"))
while i < n:
    remainder = n % i
    if remainder == 0:
        isPrime = False
        break
    else:
        i = i + 1
if isPrime:
    print("Number is Prime")
else:
    print("Number is not Prime")