Easy 2.1

fruits = ["Apple", "Orange", "Plum", "Peach"]
i = 0
while i < len(fruits):
	print((i + 1), ".", "{:>10}".format(fruits[i]))
	i = i + 1



Easy 2.2

list_a = [1, 2, 3, 4, 4, 5, 6, 0, 22]
list_b = [3, 4, 5, 6, 3, 7, 8]
for i in list_b:
	while i in list_a:
	    list_a.remove[i]
print(list_a)


Easy 2.3

a = [1, 2, 33, 23, -2, 0, 244, 66, 7]
out = []
for i in a:
	if i % 2 == 0:
		out.append(i / 4)
	else:
		out.append(i * 2)
print(out)


Normal 2.1

a = [2, -5, 8, 9, -25, 4]
out = []
for i in a:
	if i > 0:
		out.append(i)
result = []
for sqr in out:
	if int(sqr ** 0.5) ** 2 == sqr:
		result.append(int(sqr ** 0.5))
print(result)


Normal 2.2

#  Решил в принципе. Не успел доделать все даты. Все время пытался решить "Башню"

dates = {'first': '01', 'second': '02', 'third': '03', 'fourth': '04', 'fifth': '05', 'sixth': '06', 'seventh': '07', 'eight': '08'}
months = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06'}
a = input('Insert the date: ')
for key in dates:
	if dates[key] == a[0:2]:
		for mkey in months:
			if months[mkey] == a[3:5]:
				print('the', key, 'of', mkey, a[6:10])


Normal 2.3 
-(длинный вариант)

import random
i = 1
out = []
n = input("Введите целое положительное число: ")
while i <= int(n):
	number = random.randit(-100, 100)
	out.append(number)
	i = i + 1
print(out)

-короткий вариант

import random
out = []
n = input("Введите целое положительное число: ")
print([random.randint(-100, 100) for i in range(int(n))])


Normal 2.4

- первый задание

old_lst = [1, 2, 4, 5, 6, 2, 5, 2]
new_lst = list(set(old_lst))
print(new_lst)

- второе задание

old_lst = [1, 2, 4, 5, 6, 2, 5, 2]
new_lst = []
for i in old_lst:
	if old_lst.count(i) < 2:
		new_lst.append(i)
print(new_lst)


Hard 2.1

equation = 'y = -12x + 1111111140.2122'
x = 2.5
spl_result = equation.split()
number_with_x = float(spl_result[2].replace('x', '')) * x
y = number_with_x + float(spl_result[4])
print("y = " + str(y))


Hard 2.3 ("Башня")


# Не успел привести код в читаемое состояние. Не сделал комментарии. Большая часть времени ушло на решение. Работает до 20 000 000, при увеличении в 10 выдает MemoryError

room_number = input("Какая у вас комната: ")
def split(arr, size):
    arrs = []
    a = 0
    b = size
    while len(arr) >= b:

        pice = arr[a:b]
        arrs.append(pice)
        a = a + size
        b= b + size
        # arr = arr[size:]
        # arrs.append(arr)
    return arrs
n = []

for i in range(2000000):
    n.append(i + 1)
# print(n)
row_slice = []
for i in n:
    end = i ** 2
    if end <= 2000000:
        row_slice.append(end)

s = 0
num = []

for i in row_slice:
    s = s + i
    if s >= 2000000:
        break
    #
    num.append(s)



pyramid = [1]
for i in range(len(num) - 1):
    pyramid = pyramid + [n[num[i]:num[i+1]]]



floors = [[1]]
count = 1
while count < len(num):
    floors = floors + (split(pyramid[count], count + 1))
    count +=1
floor_place = [(n,x.index(int(room_number))) for n,x in enumerate(floors) if int(room_number) in x]
print(floor_place)
print("Комната находится на " + str((floor_place[0][0]) + 1) + " этаже," + str((floor_place[0][1]) + 1) + " cлева.")

