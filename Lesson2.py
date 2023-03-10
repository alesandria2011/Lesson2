#Человек вводит день и месяц своего рождения,выведите кем он является по знаку зодиака

# a = int(input("Введите число вашего рождения: "))
# b = int(input("Введите месяц вашего рождения: "))
#
# if a >= 21 and a <= 31 and b == 3 or a >= 1 and a <= 20 and b == 4:
#     print("Овен")
# elif a >= 21 and a <= 30 and b == 4 or a >= 1 and a <= 21 and b == 5:
#     print("Телец")
# elif a >= 22 and a <= 31 and b == 5 or a >= 1 and a <= 21 and b == 6:
#     print("Близнецы")
# elif a >= 22 and a <= 30 and b == 6 or a >= 1 and a <= 22 and b == 7:
#     print("Рак")
# elif a >= 23 and a <= 31 and b == 7 or a >= 1 and a <= 23 and b == 8:
#     print("Лев")
# elif a >= 24 and a <= 31 and b == 8 or a >= 1 and a <= 23 and b == 9:
#     print("Дева")
# elif a >= 24 and a <= 30 and b == 9 or a >= 1 and a <= 23 and b == 10:
#     print("Весы")
# elif a >= 24 and a <= 31 and b == 10 or a >= 1 and a <= 22 and b == 11:
#     print("Скорпион")
# elif a >= 23 and a <= 30 and b == 11 or a >= 1 and a <= 21 and b == 12:
#     print("Стрелец")
# elif a >= 22 and a <= 31 and b == 12 or a >= 1 and a <= 20 and b == 1:
#     print("Козерог")
# elif a >= 21 and a <= 31 and b == 1 or a >= 1 and a <= 18 and b == 2:
#     print("Водолей")
# elif a >= 19 and a <= 29 and b == 2 or a >= 1 and a <= 20 and b == 3:
#     print("Рыбы")
# else:
#     print("Введите число")
#






# def a_function():
#     '''Функция которая печатает текст'''
#     print('You just created a fuction!')


# a_function()


# def empty_f():
#     pass
#
# empty_f()

# Создайте функцию, которая будет считать сумму чисел в списке.


# arr = [1, 2, 3, 4]
# def s_f():
#     c = 0
#     for i in arr:
#         c += i
#     print('Сумма в списке: ', c)
# s_f()

# a = [1, 2, 3, 4]
# print(a.append(123))
# def add(a, b):
#     print('a = ', a, 'b = ', b)
#     return a + b
#
#
# # add(1, 2)
# print(add(1, 2))

# def add(a, b):
#     print('a = ', a, 'b = ', b)
#     return a + b
#
#
# print(add(1, 2))
#
# total = add(2, 2)
# print(total, type(total))
# print(add([1, 2, 3], [3, 1, 2, 1]))
# print(add('Hello ', 'World'))

# def add(a, b):
#     print('a = ', a, 'b = ', b)
#     return a + b
#
#
# print(add(b=12, a=43))

# def add(a=0, b=0):
#     print('a = ', a, 'b = ', b)
#     return a + b
#
#
# print(add(1))
# print(add(2, 3))

# def add(a, b=0, c=0):
#     print('a = ', a, 'b = ', b, 'c = ', c)
#     return a + b + c
#
#
# print(add(1))
# print(add(1, 12, 4))
# print(add(1, c=12, b=4))


# def many(*args, **kwargs):
#     # print(args)
#     for i in args:
#         print(i)
#     print(kwargs)
#     print(kwargs.values())
#
#
# many(1, 2, 3, 'ads', 23, 324, name='Diana', hello='World', num=12)


# def f_a():
#     global a
#     a = 1
#     b = 2
#     return a + b
#
#
# def f_b():
#     c = 3
#     return a + c
#
#
# print(f_a())
# print(f_b())

# def f1(a, b):
#     def f2(x):
#         return x * x * x
#
#     return f2(a) + f2(b) # (4*4*4) + (5*5*5)
#
#
# print(f1(4, 5))

# def s(a, b): return a + b
#
#
# print(s(1, 2))

# while True:
#     def is_year_leap(x):
#         if x % 4 == 0:
#             if x % 400 == 0:
#                 print('True')
#             elif x % 100 != 0:
#                 print('True')
#             else:
#                 print('False')
#         else:
#             print('False')
#
#
#     is_year_leap(int(input('Введите год: ')))
#
# ИЛИ ТАКОЕ РЕШЕНИЕ:
#
# def is_year_leap(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
# print(is_year_leap(int(input('Введите год: '))))



# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
# def calc_op( op, a, b ):
#     if op == '+':   return a + b
#     elif op == '-':   return a - b
#     elif op == '*':   return a * b
#     elif op == '/':
#         try:
#             return a / b
#         except:
#             return 'Нельзя разделить на ноль'
#
# while True:
#     op = input('Введите операцию (+, -, *, /, 0-завершение работы): ')
#     if op == '0':
#         break
#     if op in '+-*/':
#         while True:
#             try:
#                 a, b = map(float, input('a, b = ').split())
#                 print(calc_op(op, a, b))
#                 break
#             except:
#                 pass




# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
# Номер месяца вводить с клавиатуры.


# def season (num):
#     if num == 12 or 1 <= num <= 2:
#         print("Зима")
#
#     elif 3 <= num <=5:
#         print("Весна")
#
#     elif 6 <= num <=8:
#         print("Лето")
#
#     elif 9 <= num <= 11:
#         print("Осень")
#
#     else:
#         print("Неверно введен номер месяца! ")
#
# n = int(input("Введите номер месяца(1-12): "))
#
# season(n)
#

# def factorial(n):
#     if n != 0:
#         return n * factorial(n - 1)
#     else:
#         return 1
#
# print(factorial(5))
#
# def add(a, b):
#     return a + b
#
#
# variable = add(1, 2)
# print(variable)


# product = lambda x, y: x * y
#
# print(product(2, 3))

# print((lambda x: x ** 2)(4))

# power = lambda x=1, y=2: x * y
# print(power())  # 1 * 2
# print(power(2))  # x=2 2 * 2
# print(power(2, 3))  # x=2 y = 3 2 * 3

# def f1(a):
#     def f2(b):
#         return a * b
#
#     return f2
#
#
# print(f1(3)(2))

# def f1(a):
#     def f2(b):
#         return a * b
#
#     return f2
#
#
# print(f1(3)(2))
# t_f = f1(3)
# print(t_f(10))

# def f1():
#     print('Test function 1')
# def f2():
#     print('Test function 2')
# def s_d(fn):
#     def wrapper():
#         print('Start function')
#         fn()
#         print('Stop function')
#
#     return wrapper
# test_f1 = s_d(f1)
# test_f2 = s_d(f2)
#
# test_f1()
# test_f2()

# def s_d(fn):
#     def wrapper():
#         print('Start function')
#         fn()
#         print('Stop function')
#
#     return wrapper
# @s_d
# def f1():
#     print('Test function 1')
# @s_d
# def f2():
#     print('Test function 2')
# f1()
# f2()


# def s_decor(fn):
#     def wrapper(arg):
#         print('Start function: ' + str(fn.name) + ' with arg: ' + str(arg))
#         fn(arg)
#     return wrapper
# @s_decor
# def p_sqrt(num):
#     print(num ** 0.5)
# p_sqrt(4)  # 4 = num = arg


# Создайте функцию, которая принимает на вход неограниченное количество позиционных и именованных параметров,
# в качестве результата функция должна возвращать только позиционные параметры с нечетными индексами и ключевые,
# значения которых являются строками

# r = []
#
#
# def many(*args, **kwargs):
#     print(args)
#     for i in args:
#         if args.index(i) % 2 != 0:
#             r.append(i)
#     print(kwargs)
#     for value in kwargs.values():
#         if type(value) is str:
#             r.append(value)
#     print(r)
#
#
# many(1, 23, 412, 423, 'sdfs', a='hi', b=123, c='world')
#

# Написать функцию, которая заполняет массив длинной 10 элементов, случайными числами в диапазоне, указанном пользователем с клавиатуры.
# Функция должна принимать два аргумента – начало диапазона и его конец, при этом ничего не возвращать.

# import random


# def func(mn, mx):
#     arr = [random.randint(mn, mx) for i in range(10)]
#     print(arr)
#
#
# a = int(input('Начало диапазона: '))
# b = int(input('Конец диапазона: '))
# func(a, b)


# Написать функцию, которая считает сколько гласных и согласных в строке.
# Строку вводить с клавиатуры.
#
# def f(a):
#     gl = 0
#     sogl = 0
#     b = 'aouyie'
#     for i in a:
#         if i in b:
#             gl += 1
#         elif i == ' ':
#             gl += 0
#         else:
#             sogl += 1
#     return print('Гласные: ', gl, 'Согласные: ', sogl)
# f(input('Введите строку: '))
#
# class Car:
#     pass
#
#
# car_obj = Car()
# car_obj = Car()
# car_obj_2 = Car()
#
# class Car:
#     color = 'Grey'  # статическое свойство
#
#     def turn_on(self):  # метод класса
#         pass
#
#     def ride(self):  # метод класса
#         pass
#
#
# car_obj = Car()
# car_obj_2 = Car()
# print(dir(Car))
#
# class Car:
#     default_color = 'Grey'  # статическое свойство
#     def init(self, color, model):  # self - ссылка на объект класса
#         self.color = color  # динамические свойства
#         self.model = model  # динамические свойства
#     def turn_on(self):  # метод класса
#         pass
#     def ride(self):  # метод класса
#         pass
#
# car_obj = Car('Red', 'Model 1')
# car_obj_2 = Car('White', 'Model 2')
# print(car_obj.default_color, car_obj.color, car_obj.model)
# print(car_obj_2.default_color, car_obj_2.color, car_obj_2.model)
# print(dir(Car))
# s = str()

# class Car:
#     default_color = 'Grey'  # статическое свойство
#     def init(self, color, model):  # self - ссылка на объект класса
#         self.color = color  # динамические свойства
#         self.model = model  # динамические свойства
#     def turn_on(self):  # метод класса
#         pass
#     def ride(self):  # метод класса
#         pass
#     def info(self):
        # print(self.color, self.model, self.default_color)
#         return self.color, self.model, self.default_color
# car_obj = Car('Red', 'Model 1')
# car_obj_2 = Car('White', 'Model 2')
# print(car_obj.default_color, car_obj.color, car_obj.model)
# print(car_obj_2.default_color, car_obj_2.color, car_obj_2.model)
# print(car_obj.info())
# print(car_obj_2.info())
# print(dir(Car))
# s = str()


# Напишите программу с классом Car.
# Создайте динамические свойства класса Car — color (цвет), type (тип), year (год). Напишите пять методов.
# Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# Третий — присвоение автомобилю года выпуска.
# Четвертый метод — присвоение автомобилю типа.
# Пятый — присвоение автомобилю цвета

# class Car:
#     def init(self, color, type, year):  # self - ссылка на объект класса
#         self.color = color  # динамические свойства
#         self.type = type  # динамические свойства
#         self.year = year  # динамические свойства
#
#     def m1(self): print('Автомобиль заведён')
#
#     def m2(self): print('Автомобиль заглушен')
#
#     def m3(self): print('Год', self.year)
#
#     def m4(self): print('Тип', self.type)
#
#     def m5(self): print('Цвет', self.color)
#
#
# c = input('Введите цвет машины ')
# y = input('Введите год машины ')
# t = input('Введите тип машины ')
#
# car_obj = Car(c, y, t)
#
# car_obj.m1()
# car_obj.m2()
# car_obj.m3()
# car_obj.m4()
# car_obj.m5()
#
#
# Создайте класс Example. В нём пропишите 3 (метода) функции. Две переменные задайте статически, две динамически.
# Первая функция: создайте переменную внутри этой функции и выведите её
# Вторая функция: верните сумму 2-ух статичных переменных
# Третья функция: верните результат возведения первой динамической переменной во вторую динамическую переменную
# Создайте объект класса.
# Вызовите эти методы.
# Напечатайте первое статическое свойство.


# class Car:
#
#     # создание методов класса
#     def start(self):
#         print("Двигатель заведен")
#
#     def str(self):
#         return 'Car class object'
#
# car_a = Car()
# print(car_a)

# class Phone:
#
#     def init(self, color, model):
#         self.color = color
#         self.model = model
#
#     # Обычный метод
#     # Первый параметр метода - self
#     def check_sim(self, mobile_operator):
#         if self.model == 'I785' and mobile_operator == 'MTS':
#             print('Your mobile operator is MTS')
#
#
# my_phone = Phone('red', 'I785')
# my_phone.check_sim('MTS')

# class Phone:
#
#     def init(self, color, model):
#         self.color = color
#         self.model = model
#
#     # Обычный метод
#     # Первый параметр метода - self
#     def check_sim(self, mobile_operator):
#         if self.model == 'I785' and mobile_operator == 'MTS':
#             print('Your mobile operator is MTS')
#
#     # Статический метод справочного характера
#     # Возвращает хэш по номеру модели
#     # self внутри метода отсутствует
#     @staticmethod
#     def model_hash(model):
#         if model == 'I785':
#             return 34565
#         elif model == 'K498':
#             return 45567
#         else:
#             return None
#
#
# my_phone = Phone('red', 'I785')
# my_phone.check_sim('MTS')
#
# print(Phone.model_hash('I785'))
# my_phone = Phone('red', 'I785')
# print(my_phone.model_hash('K498'))


# class Phone:
#
#     def init(self, color, model):
#         self.color = color
#         self.model = model
#
#     # Метод класса
#     # Принимает 1) ссылку на класс Phone и 2) цвет в качестве параметров
#     # Создает специфический объект класса Phone(особенность объекта в том, что это игрушечный телефон)
#     # При этом вызывается инициализатор класса Phone
#     # которому в качестве аргументов мы передаем цвет и модель,
#     # соответствующую созданию игрушечного телефона
#     @classmethod
#     def toy_phone(cls, color):
#         toy_phone = cls(color, 'ToyPhone')
#         return toy_phone
#
#     # Обычный метод
#     # Первый параметр метода - self
#     def check_sim(self, mobile_operator):
#         if self.model == 'I785' and mobile_operator == 'MTS':
#             print('Your mobile operator is MTS')
#
#     # Статический метод справочного характера
#     # Возвращает хэш по номеру модели
#     # self внутри метода отсутствует
#     @staticmethod
#     def model_hash(model):
#         if model == 'I785':
#             return 34565
#         elif model == 'K498':
#             return 45567
#         else:
#             return None
#
#
# print(Phone.model_hash('I785'))
# my_phone = Phone('red', 'I785')
# print(my_phone.model_hash('K498'))
#
# my_phone.check_sim('MTS')
# Phone.toy_phone('Red')
# print(Phone.toy_phone('Red').model)
#

# Класс Human
# Создайте класс Human.
# Определите для него два статических поля: default_name и default_age.
# Создайте метод init(), который помимо self принимает еще два параметра: name и age.
# Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age.
# В методе init() определите четыре свойства: Публичные - name и age. Приватные - money и house.
# Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
# Реализуйте справочный статический метод default_info(), который будет выводить статические поля default_name и default_age.
# Реализуйте метод earn_money(), увеличивающий значение свойства money.

# class Human:
#     # Определите для него два статических поля: default_name и default_age.
#     default_name = 'John'
#     default_age = 30
#
#     # В методе __init__() определите четыре свойства: Публичные - name и age. Приватные - money и house.
#     # Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age.
#     def __init__(self, name=default_name, age=default_age):
#         self.name = name
#         self.age = age
#         self.__money = 0
#         self.__house = None
#     # Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
#     def info(self):
#         print(f'Name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Money: {self.__money}')
#         print(f'Hose: {self.__house}')
#     # Реализуйте справочный статический метод default_info(),
#     # который будет выводить статические поля default_name и default_age.
#     @staticmethod
#     def default_info():
#         print(f'Default Name: ', Human.default_name)
#         print(f'Default age: ', Human.default_age)
#
#     # Реализуйте метод earn_money(), увеличивающий значение свойства money.
#     def earn_money(self, amount):
#         self.__money += amount
#         print(f'Earn money! {self.__money}')
#
# Human.default_info()
#
# human_1 = Human('Diana', 27)
# human_1.info()
# human_1.earn_money(100)
# human_1.info()
# human_1.earn_money(100)


# Родительский класс
# class Phone:
#
#     # Инициализатор
#     def __init__(self):
#         self.is_on = False
#
#     # Включаем телефон
#     def turn_on(self):
#         self.is_on = True
#
#     # Если телефон включен, делаем звонок
#     def call(self):
#         if self.is_on:
#             print('Making call...')


# Унаследованный класс
# class MobilePhone(Phone):
#
#     # Добавляем новое свойство battery
#     def __init__(self):
#         super().__init__()
#         self.battery = 0
#
#     # Заряжаем телефон на величину переданного значения
#     def charge(self, num):
#         self.battery = num
#         print(f'Charging battery up to ... {self.battery}%')
#
#
# my_mobile_phone = MobilePhone()
# print(dir(my_mobile_phone))


# создаем класс Vehicle
# class Vehicle:
#
#     def vehicle_method(self):
#         print("Это родительский метод из класса Vehicle")
#
#
# # создаем класс Car, который наследует Vehicle
# class Car(Vehicle):
#
#     def car_method(self):
#         print("Это дочерний метод из класса Car")
#
#
# # создаем класс Cycle, который наследует Vehicle
# class Cycle(Vehicle):
#     def cycleMethod(self):
#         print("Это дочерний метод из класса Cycle")
#
#
# car_a = Car()
# car_a.vehicle_method()  # вызов метода родительского класса
# car_b = Cycle()
# car_b.vehicle_method()  # вызов метода родительского класса
#

# class Camera:
#     def camera_method(self):
#         print("Это родительский метод из класса Camera")
#     def info(self):
#         print('Camera')
# class Radio:
#     def radio_method(self):
#         print("Это родительский метод из класса Radio")
#     def info(self):
#         print('Radio')
# class CellPhone(Radio, Camera):
#     def cell_phone_method(self):
#         print("Это дочерний метод из класса CellPhone")
# cell_phone_a = CellPhone()
# cell_phone_a.camera_method()
# cell_phone_a.radio_method()
# cell_phone_a.info()
#

# Класс House
# 1. Создайте класс House
# 2. Создайте метод init() и определите внутри него два динамических свойства: _area и _price.
# 3. Свои начальные значения они получают из параметров метода init()
# 4. Создайте метод final_price(), который принимает в качестве параметра размер скидки и возвращает цену
# с учетом данной скидки.
#
# Класс SmallHouse
# 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# 2. Внутри класса SmallHouse переопределите метод init() так, чтобы он создавал объект с площадью 40м2
#
# Класс Human
#  1. Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома:
# уменьшать количество денег на счету и присваивать ссылку на только что купленный дом.
# В качестве аргументов данный метод принимает объект дома и его цену.
# 2.  Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки,
# и совершать сделку. Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры метода:
# ссылка на дом и размер скидки

# Класс House
# 1. Создайте класс House
# 2. Создайте метод __init__() и определите внутри него два динамических свойства: _area и _price.
# 3. Свои начальные значения они получают из параметров метода __init__()
# 4. Создайте метод final_price(), который принимает в качестве параметра размер скидки и
# возвращает цену с учетом данной скидки.
# class House:
#     def __init__(self, area, price):
#         self._area = area
#         self._price = price
#
#     def final_price(self, discount):
#         final_price = self._price * (100 - discount) / 100
#         print(f'Final price {final_price}')
#         return final_price
#

# Класс SmallHouse
# 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# 2. Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2
#
# Класс Human
#  1. Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома:
#  уменьшать количество денег на счету и присваивать ссылку на только что купленный дом.
#  В качестве аргументов данный метод принимает объект дома и его цену.
# 2.  Реализуйте метод buy_house(), который будет проверять, что у человека
# достаточно денег для покупки, и совершать сделку. Если денег слишком мало -
# нужно вывести предупреждение в консоль. Параметры метода: ссылка на дом и размер скидки

# class Human:
#     # Определите для него два статических поля: default_name и default_age.
#     default_name = 'John'
#     default_age = 30
#
#     # В методе __init__() определите четыре свойства: Публичные - name и age. Приватные - money и house.
#     # Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age.
#     def __init__(self, name=default_name, age=default_age):
#         self.name = name
#         self.age = age
#         self.__money = 0
#         self.__house = None
#
#     # Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
#     def info(self):
#         print(f'Name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Money: {self.__money}')
#         print(f'Hose: {self.__house}')
#
#     # Реализуйте справочный статический метод default_info(),
#     # который будет выводить статические поля default_name и default_age.
#     @staticmethod
#     def default_info():
#         print(f'Default Name: ', Human.default_name)
#         print(f'Default age: ', Human.default_age)
#
#     # Реализуйте метод earn_money(), увеличивающий значение свойства money.
#     def earn_money(self, amount):
#         self.__money += amount
#         print(f'Earn money! {self.__money}')
#
#     #  1. Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома:
#     #  уменьшать количество денег на счету и присваивать ссылку на только что купленный дом.
#     #  В качестве аргументов данный метод принимает объект дома и его цену.
#     def __make_deal(self, house, price):
#         self.__money -= price
#         self.__house = house
#
#     # 2.  Реализуйте метод buy_house(), который будет проверять, что у человека
#     # достаточно денег для покупки, и совершать сделку. Если денег слишком мало -
#     # нужно вывести предупреждение в консоль. Параметры метода: ссылка на дом и размер скидки
#     def buy_house(self, house, discount):
#         price = house.final_price(discount)
#         if self.__money >= price:
#             self.__make_deal(house, price)
#             print('Make deal!')
#         else:
#             print('Not enough money :(')
#
#
# Human.default_info()
# human_1 = Human('Diana', 27)
# human_1.info()
# human_1.earn_money(100)
# human_1.info()
# human_1.earn_money(100)
#
# house_1 = SmallHouse(300)
# human_1.buy_house(house_1, 50)
# human_1.info()



# Родительский класс
# class Phone:
#
#     def __init__(self):
#         self.is_on = False
#
#     def turn_on(self):
#         pass
#
#     def call(self):
#         pass
#
#     # Метод, который выводит короткую сводку по классу Phone
#     def info(self):
#         print(f'Class name: {Phone.__name__}')
#         print(f'If phone is ON: {self.is_on}')
#
#
# # Унаследованный класс
# class MobilePhone(Phone):
#
#     def __init__(self):
#         super().__init__()
#         self.battery = 0
#     # Такой же метод, который выводит короткую сводку по классу MobilePhone
#     # Обратите внимание, что названия у методов совпадают - оба метода называются info()
#     # Однако их содержимое различается
#     def info(self):
#         print(f'Class name: {MobilePhone.__name__}')
#         print(f'If mobile phone is ON: {self.is_on}')
#         print(f'Battery level: {self.battery}')
#

# def show_polymorphism():
#     for a in [Phone, MobilePhone]:
#         print('-------')
#         object = a()
#         object.info()
#
#
# show_polymorphism()


# Создаем список из классов
# В цикле перебираем список и для каждого элемента списка(а элемент - это класс)
# Создаем объект и вызываем метод info()
# Главная особенность: запись object.info() не дает информацию об объекте, для которого будет вызван метод info()
# Это может быть объект класса Phone, а может - объект класса MobilePhone
# И только в момент исполнения кода становится ясно, для какого именно объекта нужно вызывать метод info()




               #       Контрольная работа №3




# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]

# 2. Напишите функцию, которая проверяет: является ли слово палиндромом

# def palindrome(data):
#     data = data.replace(' ','').lower()
#     return 'Палиндром' if data == data[::-1] else 'Не палиндром'


def isPalindrome(string):
    left = 0
    right = len(string) - 1

    while right >= left:
        if not string[left] == string[right]:
            return False
        left += 1
        right -= 1
    return True


print(isPalindrome('aza'))
print(isPalindrome('vaza'))



# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)

# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая

# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.

# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай


class Tomato:
    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()


    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
        
    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        print('Gardener finished')


    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early! Your plant is green and not ripe.')


    @staticmethod
    def knowledge_base():
        print('''Harvest time for tomatoes should ideally occur
when the fruit is a mature green and
then allowed to ripen off the vine.
This prevents splitting or bruising
and allows for a measure of control over the ripening process.''')



if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()




















