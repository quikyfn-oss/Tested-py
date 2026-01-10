
#ЦИКЛЫ

'''import time

print('hello, world')
time.sleep(1)'''


'''import time

for i in range(3600):
    print('hello, world')
    time.sleep(1)'''


'''import time

for _ in range(3600):
    print('hello, world')
    time.sleep(1)'''

'''total = 0
for i in range(1, 101):
    total += i
print(total)'''


'''total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(total)'''


'''total = 0
for i in range(2, 101, 2):
    total += i
print(total)'''


'''print(sum(range(2, 101, 2)))'''


'''total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)'''

'''total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total)'''


'''total = 0
for i in range(1, 101):
    if i % 2 == 0:
        continue
    total += i
print(total)'''

#Таблица умножения
'''for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}×{j}={i * j}', end='\t')
    print()'''


'''num = int(input('пожалуйста, введите положительное целое число: '))
end = int(num ** 0.5)
is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num}-простое число')
else:
    print(f'{num}-составное')'''

'''x=int(input('введите положительное число:'))
d=int(x**0.5)
ver=True
for i in range(2,d + 1):
    if x% i ==0:
        ver=False
if ver==True:
    print(f'{x}-простое число')
else:
    print(f'{x}-составное')'''


'''x = int(input('x = '))
y = int(input('y = '))
for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        print(f'наибольший общий делитель: {i}')
        break'''

'''x = int(input('x = '))
y = int(input('y = '))
while y % x != 0:
    x, y = y % x, x
print(f'наибольший общий делитель: {x}')'''



'''import random
answer = random.randrange(1,101)
count=0
while True:
    num=int(input('Введите число:'))
    count+=1
    if num < answer:
        print('больше')
    elif num > answer:
        print('меньше')
    else:
        print('угадал правильно')
        break
print(f'Как вы догадались с {count} раз(а)')'''





