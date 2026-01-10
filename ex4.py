#№ Калькулятор ИМТ

'''h=float(input('рост(см):'))
g=float(input('вес(см):'))
imt=g/(h/100)**2
print(f'{imt =:.1f}')
if 18.5<= imt < 24:
    print('Ты в отличной форме!')
else:
    print('Ты херовый!')'''


'''height = float(input('Рост(cm)：'))
weight = float(input('Вес(kg)：'))
imt = weight / (height / 100) ** 2
print(f'{imt = :.1f}')
if 18.5 > imt:
    print('Вес слишком мал!')
elif imt>25:
    print('Вы жирный!')
elif 18.5<= imt <= 24:
    print('Вы классный!')'''

'''status_code = int(input('код состояния ответа: '))
if status_code == 400:
    description = 'Bad Request'
elif status_code == 401:
    description = 'Unauthorized'
elif status_code == 403:
    description = 'Forbidden'
elif status_code == 404:
    description = 'Not Found'
elif status_code == 405:
    description = 'Method Not Allowed'
elif status_code == 418:
    description = 'I am a teapot'
elif status_code == 429:
    description = 'Too many requests'
else:
    description = 'Unknown status Code'
print('описание кода состояния:', description)'''


'''status_code = int(input('код состояния ответа: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('Описание кода СОСТОЯНИЯ:', description)'''

'''status_code = int(input('код состояния ответа: '))
match status_code:
    case 400 | 405: description = 'Invalid Request'
    case 401 | 403 | 404: description = 'Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('Описание кода СОСТОЯНИЯ:', description)'''

'''x=float(input('x='))
if x>1:
    y = 3*x-5
elif -1<=x<=1:
    y = x+2
elif x<-1:
    y = 5*x +3
print(f'{y=}')'''


'''x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print(f'{y = }')'''


'''score = float(input('введи оценку: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print(f'{grade = }')'''


'''a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print(f'периметр: {perimeter}')
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'площадь: {area}')
else:
    print('не удается сформировать треугольник')'''

