
# Easy

# 1.1

number = input("Insert a number: ")
length = len(number)

while (length) > 0:

    n = int(number) // 10 ** (length - 1)
    print(n)

    length = length - 1

    number = int(number) % (10 ** (length))

# 1.2

a = int(input("The first number is: "))
b = int(input("The second number is: "))
c = a
a = b
b = c
print(a)
print(b)

# 1.3

age = input("How old are you? : ")
if int(age) >= 18:
    print("Access granted!")
else:
    print("Sorry, you are not old enough!")

# Normal

# 1.1

number = input("Insert a number: ")
length = len(number)
max = 0
while (length) > 0:

    n = int(number) // 10 ** (length - 1)

    if n > max:
        max = n

    length = length - 1

    number = int(number) % (10 ** (length))

print(max)

# 1.2

a = input("Give me the first number: ")
b = input("Give me the second number: ")

(a, b) = (b, a)
print(a, b)

# 1.3

a = int(input("The first factor: "))
b = int(input("The second factor: "))
c = int(input("The third factor: "))

x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a

print("x1 =", x1, "; " "x2 =", x2)

#  Hard

# переменная равна бесконечности
import math
a = math.inf

