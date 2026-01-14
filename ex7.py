'''import random

f1=0
f2=0
f3=0
f4=0
f5=0
f6=0
for _ in range(6000):
    face=random.randrange(1,7)
    if face == 1:
        f1+=1
    elif face== 2:
        f2+=1
    elif face== 3:
        f3+=1
    elif face== 4:
        f4+=1
    elif face== 5:
        f5+=1
    else:
        f6+=1
print(f'1 появилось значение {f1} раз')
print(f'2 появилось значение {f2} раз')
print(f'3 появилось значение {f3} раз')
print(f'4 появилось значение {f4} раз')
print(f'5 появилось значение {f5} раз')
print(f'6 появилось значение {f6} раз')'''

#СПИСКИ
'''list1=[35,12,99,68,55,35,87]
list2=['Python','Java','Go','Kotlin']
list3=[100,12.3,'Python']
print(list1)
print(list2)
print(list3)'''

'''items4 = list(range(1, 10))
items5 = list('hello')
print(items4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(items5)  # ['h', 'e', 'l', 'l', 'o']'''

'''items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']
print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
items5 += items6
print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]

print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]
print(items7 * 2)  # ['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']

print(29 in items6)  # True
print(99 in items6)  # False
print('C++' not in items7)     # True
print('Python' not in items7)  # False'''

'''items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0])   # apple
print(items8[2])   # pitaya
print(items8[4])   # watermelon
items8[2] = 'durian'
print(items8)      # ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
print(items8[-5])  # 'apple'
print(items8[-4])  # 'waxberry'
print(items8[-1])  # watermelon
items8[-4] = 'strawberry'
print(items8)      # ['apple', 'strawberry', 'durian', 'peach', 'watermelon']

print(items8[1:3:1])     # ['strawberry', 'durian']
print(items8[0:3:1])     # ['apple', 'strawberry', 'durian']
print(items8[0:5:2])     # ['apple', 'durian', 'watermelon']
print(items8[-4:-2:1])   # ['strawberry', 'durian']
print(items8[-2:-6:-1])  # ['peach', 'durian', 'strawberry', 'apple']

items8[1:3] = ['x', 'o']
print(items8)  # ['apple', 'x', 'o', 'peach', 'watermelon']'''

'''nums1 = [1, 2, 3, 4]
nums2 = list(range(1, 5))
nums3 = [3, 2, 1]
print(nums1 == nums2)  # True
print(nums1 != nums2)  # False
print(nums1 <= nums3)  # True
print(nums2 >= nums3)  # False'''

'''languages = ['Python', 'Java', 'C++', 'Kotlin']
for index in range(len(languages)):
    print(languages[index])'''


'''import random

counters = [0] * 6
for _ in range(6000):
    face = random.randrange(1, 7)
    counters[face - 1] += 1
# Выводят количество вхождений каждой точки
for face in range(1, 7):
    print(f'{face}{counters[face - 1]}')'''
    
