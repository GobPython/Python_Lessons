# Домашнее задание после Урока 28
# Создать класс и вызвать пять объектов этого класса.
class World:
    def __init__(self, country, city, citizen):
        self.country = country
        self.city = city
        self.citizen = citizen
    def karta(self):
        print('В городе ' + self.city + ' (' + self.country + ') проживает ' + str(self.citizen) + ' млн. жителей.')

count1 = World("Беларусь", "Минск", 3)
count2 = World('Россия', 'Москва', 10)
count3 = World('Польша', 'Варшава', 11)
count4 = World('Германия', 'Белрлин', 15)
count5 = World('Россия', 'Новосибирск', 1)

count1.karta()
count2.karta()
count3.karta()
count4.karta()
count5.karta()