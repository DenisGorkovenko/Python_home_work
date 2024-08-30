class Car:
    """Создайте класс Car с полями mass, km, power, speed, brand и реализуйте методы info() для вывода полной
        информации об автомобиле на экран. Добавьте в класс методы lock(), unlock() и соответствующие параметры,
        необходимые для этих функций. Добавьте в класс методы start_engine(), stop_engine() и соответствующие
        параметры, необходимые для этих функций."""

    def __init__(self, mass=1000, km=500, power=200, speed=180, brand='auto', access='closed', engine='off'):
        self.mass = mass
        self.km = km
        self.power = power
        self.speed = speed
        self.brand = brand
        self.access = access
        self.engine = engine

    def __str__(self):
        return (f'Brand: {self.brand}, mass: {self.mass}, km: {self.km}, power: {self.power}, speed: {self.speed},'
                f'[access: {self.access}; engine: {self.engine}]')

    def lock(self):
        if self.engine == 'on':
            return f'Невозможно закрыть автомобиль, сначала заглуши двигатель!'
        elif self.access == 'closed':
            return f'Ошибка, автомобиль уже закрыт!'
        else:
            self.access = 'closed'
            return f'Автомобиль успешно закрыт'

    def unlock(self):
        if self.access == 'open':
            return f'Ошибка, автомобиль уже открыт!'
        else:
            self.access = 'open'
            return f'Aвтомобиль успешно открыт!'

    def start_engine(self):
        if self.engine == 'on':
            return f'Ошибка, двигатель уже запущен!'
        else:
            self.engine = 'on'
            return f'Двигатель успешно запущен!'

    def stop_engine(self):
        if self.engine == 'off':
            return f'Ошибка, двигатель уже остановлен!'
        else:
            self.engine = 'off'
            return f'Двигатель успешно остановлен!'


bmw_m5 = Car(mass=1430, km=470, power=635, speed=305, brand='BMW', access='open')
kia_k5 = Car(mass=1511, km=800, power=240, speed=240, brand='KIA', engine='on')

print(bmw_m5)
print(kia_k5)

#==================================Дополнительные задания=========================================


class Book:
    """Задание 1. Создайте класс Book, который будет иметь атрибуты title, author и pages. Добавьте метод, который
    будет выводить информацию о книге в формате: "Название: [title], Автор: [author], Страницы: [pages]"."""

    def __init__(self, title='name', author='FCs', pages=350):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Название: {self.title}, Автор: {self.author}, Страницы: {self.pages}"


Tolstoy = Book(title='War and Peace', author='Leo Tolstoy', pages=736)
Dostoevsky = Book(title='The Idiot', author='Fyodor Dostoyevsky', pages=640)

print(Tolstoy)
print(Dostoevsky)


class Student:
    """Задание 2. Создайте класс Student, который будет иметь атрибуты name, age и grades (список оценок).
    Добавьте метод для вычисления среднего балла студента."""

    def __init__(self, grades, name='Ivan Ivanov', age=20):
        self.name = name
        self.age = age
        self.grades = grades

    def arithmetic_mean(self):
        result = sum(self.grades) / len(self.grades)
        return f'Средний балл = {result}'


Ivan_Ivanov = Student(grades=[5, 4, 3, 5])
print(Ivan_Ivanov.arithmetic_mean())


class Counter:
    """Задание 3. Создайте класс Counter, который будет иметь атрибут count. Реализуйте методы для увеличения,
    уменьшения и сброса счетчика."""
    def __init__(self, count=50):
        self.count = count

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def __str__(self):
        return str(self.count)


x = Counter()
print(x)
x.increment()
print(x)
x.increment()
print(x)
x.decrement()
print(x)
x.reset()
print(x)


class Rectangle:
    """Задание 4. Создайте класс Rectangle, который будет иметь атрибуты width и height. Добавьте методы для
    вычисления площади и периметра прямоугольника."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_rectangle(self):
        s = self.width * self.height
        return f'Площадь прямоугольника = {s}'

    def perimeter_rectangle(self):
        p = (self.width + self.height) * 2
        return f'Периметр прямоугольника = {p}'


rec_1 = Rectangle(2, 3)
print(rec_1.area_rectangle())
print(rec_1.perimeter_rectangle())


class Dog:
    """Задание 5. Создайте класс Dog, который будет иметь атрибуты name и age. Реализуйте метод, который выводит
    информацию о собаке, а также метод, который позволяет собаке "гавкать"."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Кличка: {self.name}; Возраст: {self.age}'

    def barking(self):
        return f'Yap Yap Yap!!!'


dog_1 = Dog('Rex', 3)
print(dog_1)
print(dog_1.barking())


class Store:
    """Задание 6. Создайте класс Store, который будет иметь атрибуты name и products (список товаров). Добавьте
    метод для добавления товара и метод для вывода всех товаров в магазине."""

    def __init__(self, name, products):
        self.name = name
        self.products = products

    def add_product(self, prod):
        self.products.append(prod)

    def print_barking(self):
        print(f'Магазин: {self.name}\nСписок товаров: {self.products}')


shop = Store('Selpo', [])
shop.add_product('tea')
shop.add_product('coffee')
shop.add_product('milk')
shop.print_barking()


class Point:
    """Задание 7. Создайте класс Point, который будет представлять точку на плоскости с координатами x и y.
    Реализуйте метод для вычисления расстояния до другой точки."""

    def __init__(self, x_point, y_point):
        self.x_point = x_point
        self.y_point = y_point

    def dist(self, other):
        return (f'Расстояние между точками: '
                f'{((self.x_point - other.x_point) ** 2 + (self.y_point - other.y_point) ** 2) ** 0.5}')


p1 = Point(1, 2)
p2 = Point(4, 3)

print(p1.dist(p2))


class Person:
    """Задание 8. Создайте класс Person, который будет иметь атрибуты first_name, last_name и age. Реализуйте метод,
    который выводит полное имя человека и его возраст."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"Сотрудник: {self.first_name} {self.last_name}, Возраст: {self.age}"


person_1 = Person('Иван', 'Петров', 34)

print(person_1)


class BankAccount:
    """Задание 9. Создайте класс BankAccount, который будет иметь атрибуты account_number и balance. Реализуйте
    методы для пополнения счета, снятия денег и проверки баланса."""
    
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def add_balance(self, summa):
        self.balance += summa
        return self.balance

    def withdraw(self, summa):
        if self.balance < summa:
            print(f'Недостаточно средств!!!')
        else:
            self.balance -= summa
        return self.balance

    def deposit(self):
        print(f'На счете {self.account_number} - {self.balance} р.')


my_bank_account = BankAccount(123321)
my_bank_account.deposit()
my_bank_account.withdraw(4500)
my_bank_account.add_balance(10000)
my_bank_account.deposit()
my_bank_account.withdraw(4500)
my_bank_account.deposit()
