class MyClass:
    name = 'Class MyClass'

    def set(self, n):
        self.nickname = n

    def get(self):
        print('Значение поля: ', self.nickname)

    def __init__(self, n):
        self.set(n)
        print('Создан экземпляр класса')
        self.get()

green = MyClass('Зеленый')
print('Принадлежность: ', green.name)

red = MyClass('Красный')
print('Принадлежность: ', red.name)


MyClass.name = 'Здесь могла быть Ваша реклама'
print('Спрашивает красный: ', red.name)
print('Спрашивает Зелёный: ', green.name)