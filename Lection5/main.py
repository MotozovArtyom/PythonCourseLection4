def deco(func): # Декоратор объявляется как обычная функция, которая принмает на вход функцию. Возможна передача доп .аргументов
    print("Hello {0}".format(func.__name__))
    return func
# Декораторы на вход принимают функцию. Могут вытащить из неё аргументы, имя, состояние и много другого
# Декораторы должны возвращать ссылку на функцию

@deco #Декоратор функции пишется через символ @ (собака)
def my_func(a, b, c):
    print("Call my_func")

# ООП - Объектно Ориентированное Программирование
# Класс - шаблон по которому создаются объекты.
# В классе описываются:
#   *артибуты(переменная-член, переменная класса)
#   *методы (функции-члены, функции-класса)
# Классы представляют информационную модель из реальной жизни.
#
# 6 основ ООП:
# 1. Инкапсуляция - сокрытие реализации от пользователя
# 2. Наследование - наследование классов
# 3. Полиморфизм - одно имя функции, много форм. Поведение выбирается на основе количества и типа переменных
# 4. Посыл сообщения - Вызов методов
# 5. Повтор кода - все выше перечисленное помогает сократить написание кода программы
# 6. Абстракция - описание классов, абстрагирование от реального мира
# Иногда Абстракцию ставят выше всего (и это рационально, т.к. при разработке ПО сначала ведется создание классов,
# а потом уже сокрываются переменные


# Классы могут наследоваться от других классов. class ClassName(SuperClassName,...):pass
# self - это ссылка на объект, от которого был вызван метод или атрибут. (ссылка на самого себя)
# Аналог this в C++, Java
#
# Атрибуты в классах должны быть private, а методы public
# Для манипулирования атрибутами вне класса существуют два метода, которые имеют специальное название:
# геттер и сеттер (getter & setter) (получить и установить)
# Getter позволяет получить значение атрибута
# Setter позволяет изменить значение атрибута
# Классы, атрибуты, методы, функции, переменные именуем в CamelCase style,
# атрибуты, методы, функции и переменные именуем в sneak_case_style
class MyClass: # Класс
    def __init__(self, a=0, b=10):  # Конструктор
        self.a = a  # self.a - атрибут класса MyClass, a - аргумент метода
        self.b = b  # Артибут класса
        self.pub = 0 # public - артибут доступен всем
        self._prot = 10 # protected - атрибут доступен классу и его подклассам
        self.__priv = 100 # private - атрибут доступен только классу

    def getA(self):  # Геттер
        return self.a

    def setA(self, a):  # Сеттер
        self.a = a

    def getB(self):
        return self.b

    def setB(self, b):
        self.b = b


if __name__ == '__main__':
    my_func(1, 2, 3)
    obj = MyClass()
    print(obj._prot)
    print(obj.pub)
    print(obj.__priv)
    print(obj._MyClass__priv)
