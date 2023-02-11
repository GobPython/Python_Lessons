# Домашнее задание после Урока 29
# Создайте класс на тему животных. В классе должен присутствовать конструктор не менее трёх методов.
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
        print('Популяция:' + str(self.size) + ' особей.')

opisanie1 = Animals ('Кошка', 'везде, кроме крайнего Севера и Юга', 175468324)
opisanie1.first()
opisanie1.second()
opisanie1.third()
