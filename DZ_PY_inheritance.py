class Dog:
    """Задание 1. Создайте базовый класс Dog, который будет иметь атрибуты name и age. Затем создайте подклассы
    WorkingDog (с атрибутом job) и PetDog. Реализуйте методы, которые выводят информацию о работе собаки или о том,
    как она ведет себя как домашний питомец."""

    def __init__(self, name, age):
        self.name = name
        self.age = age


class WorkingDog(Dog):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def __str__(self):
        return f'Кличка: {self.name}, Специальность: {self.job}'


class PetDog(Dog):
    def __init__(self, name, age, character):
        super().__init__(name, age)
        self.character = character

    def __str__(self):
        return f'Кличка: {self.name}, Характер: {self.character}'


dog_1 = WorkingDog('Дружок', 4, 'Спасатель')
dog_2 = PetDog('Стрелка', 2, 'Дружелюбная')

print(dog_1)
print(dog_2)


class Vehicle:
    """Задание 2. Создайте базовый класс Vehicle, который будет иметь атрибуты make, model и year. Затем создайте
    подклассы Car и Truck, добавив атрибуты, специфичные для каждого типа (например, passenger_capacity для автомобиля
    и payload_capacity для грузовика). Реализуйте метод для отображения информации о транспортном средстве."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Производитель: {self.make}, Модель: {self.model}, Год выпуска: {self.year}"


class Car(Vehicle):
    def __init__(self, make, model, year, passenger_capacity):
        super().__init__(make, model, year)
        self.passenger_capacity = passenger_capacity

    def __str__(self):
        return f"{super().__str__()}, Количество пассажиров: {self.passenger_capacity}"


class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def __str__(self):
        return f"{super().__str__()}, Грузоподъемность: {self.payload_capacity}"


car_1 = Car('Toyota', 'Corolla', 2020, 5)
truck_1 = Truck('Volvo', 'FH16', 2016, 40000)

print(car_1)
print(truck_1)


class Animal:
    """Задание 3. Создайте базовый класс Animal, который будет иметь атрибуты name и species. Затем создайте подклассы
    Mammal и Bird, добавив методы, специфичные для каждого класса (например, метод make_sound() для млекопитающих и
    метод fly() для птиц)."""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f'Наименование: {self.name}, Вид: {self.species}'


class Mammal(Animal):
    def __init__(self, name, species, make_sound):
        super().__init__(name, species)
        self.make_sound = make_sound

    def __str__(self):
        return f"{super().__str__()}, Издаваемый звук: {self.make_sound}"


class Bird(Animal):
    def __init__(self, name, species, fly):
        super().__init__(name, species)
        self.fly = fly

    def __str__(self):
        return f"{super().__str__()}, Возможность летать: {self.fly}"


animal_1 = Mammal('Dog', 'Canidae', 'barking')
animal_2 = Bird('Chicken', 'Bankivsky rooster', 'No')

print(animal_1)
print(animal_2)


class Toy:
    """Задание 4. Создайте базовый класс Toy, который будет иметь атрибуты name и price. Затем создайте подклассы
    ActionFigure и BoardGame, добавив атрибуты, специфичные для каждого типа (например, character_name для фигурки и
    number_of_players для настольной игры). Реализуйте метод для вывода информации о каждой игрушке."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Название: {self.name}, Стоимость: {self.price}"


class ActionFigure(Toy):
    def __init__(self, name, price, character_name):
        super().__init__(name, price)
        self.character_name = character_name

    def __str__(self):
        return f"{super().__str__()}, Имя персонажа: {self.character_name}"


class BoardGame(Toy):
    def __init__(self, name, price, number_of_players):
        super().__init__(name, price)
        self.number_of_players = number_of_players

    def __str__(self):
        return f"{super().__str__()}, Количество игроков: {self.number_of_players}"


toy_1 = ActionFigure('Супергерой', 1200, 'Batman')
toy_2 = BoardGame('Carcassonne', 5000, 6)

print(toy_1)
print(toy_2)


class Event:
    """Задание 5. Создайте базовый класс Event, который будет иметь атрибуты event_name, date и location. Затем
    создайте подклассы Concert и Conference, добавив атрибуты, специфичные для каждого типа (например, performer для
    концерта и speakers для конференции). Реализуйте метод для отображения информации о событии."""

    def __init__(self, event_name, date, location):
        self.event_name = event_name
        self.date = date
        self.location = location

    def __str__(self):
        return (f"Название мероприятия: {self.event_name}, Дата проведения: {self.date}, "
                f"Место проведения: {self.location}")


class Concert(Event):
    def __init__(self, event_name, date, location, performer):
        super().__init__(event_name, date, location)
        self.performer = performer

    def __str__(self):
        return f"{super().__str__()}, Исполнитель: {self.performer}"


class Conference(Event):
    def __init__(self, event_name, date, location, speaker):
        super().__init__(event_name, date, location)
        self.speaker = speaker

    def __str__(self):
        return f"{super().__str__()}, Докладчик: {self.speaker}"


event_1 = Concert('"Живой звук"', '24.06.24', 'Локомотив-Арена', 'Ленинград')
event_2 = Conference('Конференция', '12.12.24', 'ДКЖ', 'С. Шнуров')

print(event_1)
print(event_2)