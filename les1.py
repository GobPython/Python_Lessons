# Домашнее задание после Уроков 18 и 19

# 1. Дано 2 множества, содержащих названия IT-компаний.
# Найти только те компании, которые содержатся в обоих множествах.
mn1 = {'Microsoft', 'Oracle', 'Google'}
mn2 = {'Apple', 'NVidia', 'Oracle', 'Google'}
print(mn1, '\n', mn2)
print(mn1&mn2)

# 2. Сгенерировать n множеств. Вывести множества кратные трём и не входящие в первое множество.
import random
a = int(input('Введите длину множества\n'))
set1 = set()
set2 = set()
while len(set1) < a:
    set1.add(random.randint(1, 100))
print(set1, '\nПеребеираем случайные числа для формирования нового множества\n')
while len(set2) < a:
    b = random.randint(1, 100)
    print(b)
    if b % 3 == 0 and b not in set1:
        set2.add(b)
        # len2 += 1
print(set2)
