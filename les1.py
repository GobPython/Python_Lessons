# Домашнее задание после Урока 11
# Задание № 1.1
print('Обрабатываем ValueError')
import  math
f = input('Введите число:\n')
try:
    print(math.sqrt(float(f)))
except ValueError:
    print('Просим вводить только числа, неотрицательные.')
finally:
    print('\nПодождите пожалуйста 1 секунду')
import time
time.sleep(1)

# Задание № 1.2
print('\n\nОбрабатываем TypeError')
a = 2
b = 'f'
print('Первая переменная - число.')
print('Вторая переменная - буква.\n')
try:
    c = a + b
except TypeError:
    print('Сложение переменных типа строка и цифра - невозможно')
finally:
    print('Ну как-то так в общем')

print('\n\nПодождите пожалуйста 3 секунды. Не нажимайте никаких клавиш, до того, как Вас попросят ввести данные.')
import time
time.sleep(3)

# Задание № 2
import datetime
today = datetime.datetime.now()
x = today.year
y = today.month
z = today.day
print('Сегодня ',z, y, x)
print('Вычисляем возраст (полных лет).\n'
      'Введите Вашу дату рождения в соответствии со следующими инструкциями.')
try:
    u = input('\nВведите Ваш год рождения в формате ГГГГ: ')
    a = int(u)
    v = input('\nВведите Ваш месяц рождения в формате ММ: ')
    b = int(v)
    w=  input('\nВведите Ваш день рождения в формате ДД: ')
    c = int(w)
    if a<=0 or b<=0 or c<=0:
        print('\nВведено отрицательное число или число равное нулю. Год/месяц/день должны быть больше нуля.')
    else:
        if b>y or b==y and c>z:
            print('Ваш возраст - ', x-a-1)
        else:
            print('Ваш возраст - ', x-a)
except ValueError:
    print('Просим вводить год/месяц/дату цифрами.')

