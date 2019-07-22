import random

def queen_position (i, j):
    return [i, j]

desk = []
for _ in range(1, 9):
    a = random.randint(1, 8)
    b = random.randint(1, 8)
    desk = desk + [queen_position(a, b)]
print(desk)                               # список из координат всех восьми ферзей


flag = False
for count in range(1, 8):
    k = count
    while k > 0:
        if desk[k -1][0] != desk[k][0] and desk[k -1][1] != desk[k][1] and desk[k - 1][0] - desk[k][0] != desk[k - 1][1] - desk[k][1]:  # проверяем по трем условиям: вертикаль, горизонталь, диагональ

            desk[k], desk[k -1] = desk[k -1], desk[k]                          
            k -= 1
            print(desk)                                  # для контроля принтуем список сравниваемых координат

        else:
            print("yes")                                 # ферзи бьют 
            flag = True
            break
    if flag:
        break

    
        print("no")                                 