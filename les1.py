# Домашнее задание после Урока 21
# 1. В текстовый файл построчно записаны фамилия и имя каждого учащегося класса и
# их оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3 баллов,
# и посчитать средний балл по классу.
print('Результат выполнения задания 1\n')
with open("less21.txt", 'r', encoding='utf-8') as file:
    list1 = file.read()
    # print(type(list1))
    print('Список учеников и их оценок за контрольную:\n', list1, sep='')
    list1 = list1.replace('\n', ' ')
    list2 = list1.split(' ')
    # print(list2, type(list2))
    # print((len(list2)))
    item = 2
    foraverage = 0
    print('\nУченики, оценка которых менее 3:')
    while item <= len(list2):
        if int(list2[item]) < 3:
             print(list2[item-2], list2[item-1])
        foraverage += int(list2[item])
        item += 3
    print('\nСредняя оценка по классу', round(foraverage / (len(list2) / 3), 2))

# 2. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.
print('\nРезультат выполнения задания 2\n')
with open('less21_1.txt', 'w') as file:
    while True:
        str_for_file = input('Введите строку: ')
        file.write(str_for_file)
        file.write('\n')
        if str_for_file == "":
            print('Ввод строк окончен.\nПрограмма завершена.')
            break