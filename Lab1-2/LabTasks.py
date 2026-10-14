wmarks = int(input("Enter marks (1-100): "))

if marks < 50:
    grade = "F"
elif marks <= 60:
    grade = "E"
elif marks <= 70:
    grade = "D"
elif marks <= 80:
    grade = "C"
elif marks <= 90:
    grade = "B"
else:
    grade = "A"

print("Grade:", grade)

#Task 2: Factorial of a number
print("Activity 2: Factorial of a number")
num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    i = 1
    while i <= num:
        factorial = factorial * i
        i = i + 1
    print("The factorial of", num, "is", factorial)


#Task 3: Fibonacci series
print("Activity 3: Fibonacci series")
terms = int(input("How many terms? "))

a, b = 0, 1
count = 0
series = []

while count < terms:
    series.append(a)
    a, b = b, a + b
    count = count + 1

print(*series)