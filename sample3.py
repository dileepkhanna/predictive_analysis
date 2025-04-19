from abc import ABC, abstractmethod
class Animal(ABC):
    def sleep(self):
        print("I am going to sleep")

    @abstractmethod
    def sound(self):
        print("This function is for defining the sound")
    # pass
class Dog(Animal):
    def sound(self):
        print("I can break")
class Rabbit(Animal):
    def sound(self):
        super().sound()
        print("I can squeak")
# r = Rabbit()
# r.sound()
a = Rabbit()
a.sleep()
a.sound()
