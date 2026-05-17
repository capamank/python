from abc import ABC,abstractmethod
 
class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass #doesnt make any task in this function in this class
class lion(animal):
    def make_sound(self):
        print("roar")

class cow(animal):
    def make_sound(self):
        print("moooooo")
lion=lion()
lion.make_sound()
cow=cow()
cow.make_sound()
