1.1

number = input("Insert a number: ")
length = len(number)

while (length) > 0:

    n = int(number) // 10 ** (length - 1)
    print(n)

    length = length - 1

    number = int(number) % (10 ** (length))

1.2

a = int(input("The first number is: "))
b = int(input("The second number is: "))
c = a
a = b
b = c
print(a)
print(b)

1.3

age = input("How old are you? : ")
if int(age) >= 18:
    print("Access granted!")
else:
    print("Sorry, you are not old enough!")