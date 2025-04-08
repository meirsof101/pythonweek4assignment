# Parent class
class Vehicle:
    def move(self):
        raise

# Child class 1: Car
class Car(Vehicle):
    def move(self):
        print("Driving")

# Child class 2: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying")

# Child class 3: Animal
class Animal:
    def move(self):
        raise
# Child class 4: Dog
class Dog(Animal):
    def move(self):
        print("Running")
# Child class 5: Bird
class Bird(Animal):
    def move(self):
        print("Flying")

# Creating instances of vehicles and animals
my_car = Car()
my_plane = Plane()
my_dog = Dog()
my_bird = Bird()

# Calling the move method for each object
my_car.move()    # Output: Driving 
my_plane.move()  # Output: Flying 
my_dog.move()    # Output: Running
my_bird.move()   # Output: Flying 
