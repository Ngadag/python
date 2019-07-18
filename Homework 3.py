3.1 Easy.

def my_round(number, ndigits):
    split_ = str(number).split('.')
    if len(split_[1]) <= (ndigits - 1):
        return number
    else:
        if int(split_[1][ndigits]) > 5:
            fraction_round = int(split_[1][0:ndigits]) + 1
            if split_[1][0:ndigits] == '9' * ndigits :
                num_new = int(split_[0]) + 1
                return (str(num_new)+ "." + '0' * ndigits)
                print(fraction_round)
            else:
                return(split_[0] + "." + str(fraction_round))
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(round(2.1234567, 5))
print(round(2.1999967, 5))
print(round(2.9999967, 5))


3.2 Easy

def lucky_ticket(ticket_number):
    sum1 = 0
    sum2 = 0
    if len(str(ticket_number)) != 6:
        return('Неверный номер!')
    i = 1
    while i < 4:
        sum1 = sum1 + ticket_number % 10
        ticket_number = ticket_number // 10
        i = i + 1
    while 7 > i >= 4:
        sum2 = sum2 + ticket_number % 10
        ticket_number = ticket_number // 10
        i = i + 1
    if sum1 == sum2:
        return('Счастливый билет!')
    else:
        return('Не повезло!')

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))


3.1 Normal

def fibo_n_m(n, m):
    fibo = [1, 1]
    i = 0
    while i < m + 1:
        fibo.append(fibo[i] + fibo[i+1])
        i +=1
    return fibo[n-1:m]

print(fibo_n_m(3, 14))


3.2 Normal


def bubble_sort(given_list):
    """сортировка списка А методом пузырька"""
    n = len(given_list)
    for bypass in range(1, n):
        for k in range(0, n-bypass):
            if given_list[k] > given_list[k+1]:
                given_list[k], given_list[k+1] = given_list[k+1], given_list[k]
    return given_list
my_list = [1, 4, 2, 67, 5, 87, 2, -9]
print(bubble_sort(my_list))


3.4 Normal

def if_para(a1, a2, a3, a4):
    result = list(zip(a1, a2, a3, a4))
    side1 = abs(result[0][0] - result[0][1])
    side2 = abs(result[1][0] - result[1][1])
    side3 = abs(result[0][2] - result[0][3])
    side4 = abs(result[1][2] - result[1][3])
    base1 = abs(result[0][0] - result[0][2])
    base2 = abs(result[1][0] - result[1][2])
    base3 = abs(result[0][1] - result[0][3])
    base4 = abs(result[1][1] - result[1][3])

    if side1 == side3 and side2 == side4:
        if base1 == base3 and base2 == base4:
            return print('Это параллелограмм!')
        else:
            return print('Это не параллелограмм!')
    else:
        return print('Это не параллелограмм!')

# Test 1

x1 = [7, -1]
x2 = [8, 2]
x3 = [10, -2]
x4 = [11, 1]
if_para(x1,x2,x3,x4)

# Test 2

x1 = [-2, 1]
x2 = [-2, 3]
x3 = [2, -1]
x4 = [2, 1]
if_para(x1,x2,x3,x4)

# Test 3

x1 = [2, -6]
x2 = [3, -4]
x3 = [6, -6]
x4 = [5, -4]
if_para(x1,x2,x3,x4)


