'''print(321 + 12) # сложение
print(321 - 12) # вычитание
print(321 * 12) # умножение
print(321 / 12) # деление
print(321 // 12) # дробное деление
print(321 % 12)  # Делениие по модулю (целочисленное)
print(321 ** 12) # Возведение в степень'''


'''print(2 + 3 * 5)           # 17
print((2 + 3) * 5)         # 25
print((2 + 3) * 5 ** 2)    # 125
print(((2 + 3) * 5) ** 2)  # 625'''



'''a = 10
b = 3
a += b        # a = a + b
a *= a + 2     # a = a * (a + 2)   #ОПЕРАТОРЫ ПРИСВАИВАНИЯ
print(a)'''


'''# SyntaxError: invalid syntax
# print((a = 10))
print((a := 10))  # 10
print(a)          # 10'''


'''flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print('flag0 =', flag0)     # flag0 = True
print('flag1 =', flag1)     # flag1 = True
print('flag2 =', flag2)     # flag2 = False
print('flag3 =', flag3)     # flag3 = False
print('flag4 =', flag4)     # flag4 = True
print('flag5 =', flag5)     # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)      # False'''


'''f = float(input(':введите температуру в градусах Фаренгейта '))
c = (f - 32) / 1.8    # в выводе будет отображаться одна цифра после десятичной точки. 
print('%.1f градусов по Фаренгейту = %.1f градусов Цельсия' % (f, c))'''


'''f = float(input('введите температуру в градусах Фаренгейта: '))
c = (f - 32) / 1.8
print(f'{f:.1f}Градусов по Фаренгейту = {c:.1f}Градусов Цельсия')'''


'''radius = float(input('пожалуйста, введите радиус окружности: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('perimeter: %.1f' % perimeter)
print('Площадь: %.1f' % area)'''


'''import math

radius = float(input('Пожалуйста, введите радиус окружности: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'периметр: {perimeter:.2f}')
print(f'площадь: {area:.2f}')'''


'''year = int(input('пожалуйста, введите год: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f'{is_leap = }')'''