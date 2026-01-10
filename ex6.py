'''for num in range(2, 100):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)'''

'''a, b = 0, 1
for _ in range(20):
    a, b = b, a + b
    print(a)'''

#Число нарцисса
'''for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)'''



'''num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)'''


'''for x in range(0, 21):
    for y in range(0, 34):
        for z in range(0, 100, 3):
            if x + y + z == 100 and 5 * x + 3 * y + z // 3 == 100:
                print(f'петух: {x} только, курица: {y} только, цыпленок: {z} только')'''


'''import random

money=1000
while money>0:
    print(f'Ваш общий капитал: {money} долларов')


    while True:
        debt=int(input('Сделайте ставку! '))
        print(f'Ставка принята,ставок больше нет.')
        if 0 < debt <= money:
            break

    first_point= random.randrange(1,7)+random.randrange(1,7)
    print(f'Выбросил кости')

    if first_point ==7 or first_point == 11:
        print(f'Игрок победил')
        money +=debt
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print('Дилер победил!')
        money -=debt
    else:
        while True:
            current_point=random.randrange(1,7)+random.randrange(1,7)
            print(f'Игрок выбросил {current_point} очков')

            if current_point == 7:
                print('Дилер выиграл!\n')
                money -= debt
                break
            elif current_point == first_point:
                print('Игрок выиграл!\n')
                money += debt
                break
print('Вы обанкротились, игра окончена!')'''