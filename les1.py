# Домашнее задание после Практического занятия "Числа и обработчик исключений"
# за основу возьму предыдущее домашнее задание (после урока 11)
import datetime
today = datetime.datetime.now()
x = today.year
y = today.month
z = today.day
print('Прагамма сравнения возрастов Сергея и Андрея'
      '\nСегодня ',z, y, x)
print('\nВычисляем возраст Сергея (полных лет).\n'
      'Введите дату рождения Сергея в соответствии со следующими инструкциями.')
try:
    u = input('\nВведите год рождения Сергея в формате ГГГГ: ')
    a = int(u)
    v = input('\nВведите месяц рождения Сергея в формате ММ: ')
    b = int(v)
    w=  input('\nВведите день рождения Сергея в формате ДД: ')
    c = int(w)
    if a<=0 or b<=0 or c<=0:
        print('\nВведено отрицательное число или число равное нулю. Год/месяц/день должны быть больше нуля.\nПрограмма остановлена')
        exit(0)
    else:
        if b>y or b==y and c>z:
            A = x-a-1
            print('Возраст Сергея - ', A)
        else:
            A = x-a
            print('Возраст Сергея - ', A)
except ValueError:
    print('\nПросим вводить год/месяц/дату цифрами.\nПрограмма остановлена')
    exit(0)

print('\nВычисляем возраст Андрея (полных лет).\n'
      'Введите дату рождения Андрея в соответствии со следующими инструкциями.')
try:
    r = input('\nВведите год рождения Андрея в формате ГГГГ: ')
    d = int(r)
    s = input('\nВведите месяц рождения Андрея в формате ММ: ')
    e = int(s)
    t=  input('\nВведите день рождения Андрея в формате ДД: ')
    f = int(t)
    if d<=0 or e<=0 or f<=0:
        print('\nВведено отрицательное число или число равное нулю. Год/месяц/день должны быть больше нуля.\nПрограмма остановлена')
        exit(0)
    else:
        if e>y or e==y and f>z:
            B = x-d-1
            print('\nВозраст Андрея - ', B)
        else:
            B = x-d
            print('\nВозраст Андрея - ', B)
except ValueError:
    print('\nПросим вводить год/месяц/дату цифрами.\nПрограмма остановлена')
    exit(0)

if A>B or A==B and b<e or A==B and b==e and c<f:
    print('\nСергей старше Андрея')
elif a==d and b==e and c==f:
        print('\nСергей и Андрей родились в один день.')
else:
    print('\nАндрей старше Сергея')