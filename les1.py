# Домашнее задание после Уроков 32 и 33
# В наследниках класса из предыдущего урока переопределить методы из класса родителя,
# а также добавить не менее трёх значений по умолчанию.

# Урок 29. Создайте класс на тему животных. В классе должен присутствовать конструктор не менее трёх методов.
class Animals:
    def __init__(self, type, area, size):
        self.type = type
        self.area = area
        self.size = size
    def first(self):
        print('Вид животного: ' + self.type)
    def second(self):
        print('Место обитания: ' + self.area)
    def third(self):
        print('Популяция:' + str(self.size) + ' особей.\n')

opisanie1 = Animals ('Кошка', 'везде, кроме крайнего Севера и Юга', 175468324)
opisanie1.first()
opisanie1.second()
opisanie1.third()

# Урок 30. В класс из предыдущего урока добавьте три класса-наследника на ваше усмотрение.

class Fly(Animals):
    def __init__(self, type, area = 'Европа', size = 1111111):
        super().__init__(type, area, size)
    def first(self):
        print('Вид птицы: ' + self.type)
    def second(self):
        print('Место гнездования: ' + self.area)
    def third(self):
        print('Количество цыплят:' + str(self.size))
    def fly(self):
        print('Это летающая птица.\n')
class Water(Animals):
    def __init__(self, area, size, type = 'Гагара'):
        super().__init__(type, area, size)
    def first(self):
        print('Вид птицы: ' + self.type)
    def second(self):
        print('Место гнездования: ' + self.area)
    def third(self):
        print('Количество цыплят:' + str(self.size))
    def _water(self):
        print('Это водоплаващая птица.\n')

class NoFly(Animals):
    def __init__(self, area, type = 'Пингвин', size = 3333333):
        super().__init__(type, area, size)
    def first(self):
        print('Вид птицы: ' + self.type)
    def second(self):
        print('Место гнездования: ' + self.area)
    def third(self):
        print('Количество цыплят:' + str(self.size))
    def __nofly(self):
        print('Это нелетающая птица.')

bird1 = Fly('Голубь')
bird1.first()
bird1.second()
bird1.third()
bird1.fly()
bird2 = Water('Евразия', 2222222)
bird2.first()
bird2.second()
bird2.third()
bird2._water()
bird3 = NoFly(area = 'Южный полюс')
bird3.first()
bird3.second()
bird3.third()
bird3._NoFly__nofly()

