# 089 - Viết chương trình để sử dụng trừu tượng trong Python

from abc import ABC, abstractmethod

# Lớp cơ sở Animal với phương thức trừu tượng sound
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Lớp Dog kế thừa từ lớp Animal, ghi đè phương thức sound
class Dog(Animal):
    def sound(self):
        return "Woof!"

# Lớp Cat kế thừa từ lớp Animal, ghi đè phương thức sound
class Cat(Animal):
    def sound(self):
        return "Meow!"

# Tạo đối tượng từ lớp Dog và Cat
dog = Dog()
cat = Cat()

# Gọi phương thức sound của đối tượng Dog và Cat
print(dog.sound())
print(cat.sound())