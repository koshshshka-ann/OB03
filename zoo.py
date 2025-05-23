#Задание
# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.

# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

# Родительский класс животных
class Animal:
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} ест {self.food}")

# Класс птиц
class Bird(Animal):
    def __init__(self, name, age, food, fly_ability): # спец. атрибут - способность летать
        super().__init__(name, age, food)
        self.fly_ability = fly_ability

    def make_sound(self):
        print(f"{self.name} чирикает: Чик-чирик!")

# Класс млекопитающих
class Mammal(Animal):
    def __init__(self, name, age, food, fur_thickness): # спец. атрибут - густота шерсти
        super().__init__(name, age, food)
        self.fur_thickness = fur_thickness

    def make_sound(self):
        print(f"{self.name} рычит: Р-р-р-р-р!")

#Класс пресмыкающихся
class Reptile(Animal):
    def __init__(self, name, age, food, body_length): # спец. атрибут - длина тела
        super().__init__(name, age, food)
        self.body_length = body_length

    def make_sound(self):
        print(f"{self.name} шипит: Ш-ш-ш-ш-ш!")

# Полиморфизм
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Смотрители зоопарка
class Zookeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"Смотритель зоопарка {self.name} кормит {animal.name}")

# Ветеринары
class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"Ветеринар {self.name} лечит {animal.name}")

# Класс Zoo с композицией
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_staff(self, employee):
        self.staff.append(employee)
        print(f"Сотрудник {employee.name} принят на работу")

    def show_animals(self):
        print("\nСписок животных в зоопарке:")
        for animal in self.animals:
            print(f"{animal.name} ({animal.__class__.__name__})")

    def show_staff(self):
        print("\nСписок сотрудников зоопарка:")
        for employee in self.staff:
            print(f"{employee.name} ({employee.__class__.__name__})")

# === Демонстрация работы ===

# Создаем животных
bird = Bird("Попугай Кеша", 5, "зерно", True)
mammal = Mammal("Кошка Фифа", 12, "сухой корм", "hairless")
reptile = Reptile("Крокодил Гена", 28, "рыбу", 2.5)

# Создаем сотрудников
keeper = Zookeeper("Вася")
vet = Veterinarian("Петя")

# Создаем зоопарк и добавляем животных и сотрудников
zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_staff(keeper)
zoo.add_staff(vet)

# Демонстрируем полиморфизм
print("\nЗвуки животных:")
animal_sound(zoo.animals)

#Демонстрируем работу сотрудников
keeper.feed_animal(bird)
vet.heal_animal(reptile)
