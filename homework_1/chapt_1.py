class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} издаёт звук: {self.sound}")

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Гав-гав")
        self.color = color

    def make_sound(self):
        print(f"Собака {self.name} (цвет: {self.color}) говорит: {self.sound}")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Мяу-мяу")
        self.color = color

    def make_sound(self):
        print(f"Кошка {self.name} (цвет: {self.color}) говорит: {self.sound}")

class Bird(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Чирик-чирик")
        self.color = color

    def make_sound(self):
        print(f"Птица {self.name} (цвет: {self.color}) говорит: {self.sound}")

my_dog = Dog(name="Шарик", color="Белый")
my_cat = Cat(name="Мурка", color="Серый")
my_bird = Bird(name="Кеша", color="Зелёный")

my_dog.make_sound()
my_cat.make_sound()
my_bird.make_sound()
