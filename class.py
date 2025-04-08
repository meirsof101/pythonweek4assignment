# Class
class Watch:
    color = "black" 
    def ticking(self):
        print("The watch is ticking")
my_watch = Watch()
print(my_watch.color) 

# Attributes and Method
class Watch:
    def __init__(self, color, brand, is_digital=True):
        self.color = color
        self.brand = brand
        self.is_digital = is_digital

    def ticking(self):
        print("The watch is ticking")
my_watch = Watch("black", "Rolex", True)
print(my_watch.color)
print(my_watch.brand)
print(my_watch.is_digital)
my_watch.ticking()

#Constructors
class Watch:
    def __init__(self, color, brand, is_digital=True):
        self.color = color
        self.brand = brand
        self.is_digital = is_digital

    def ticking(self):
        print(f"{self.brand} watch is ticking...")

# Creating instances of the Watch class
watch1 = Watch("black", "Rolex", True)
watch2 = Watch("silver", "Casio", False)
watch3 = Watch("blue", "Samsung", True)

# Accessing attributes
print(f"Watch 1: {watch1.color}, {watch1.brand}, Digital: {watch1.is_digital}")
print(f"Watch 2: {watch2.color}, {watch2.brand}, Digital: {watch2.is_digital}")
print(f"Watch 3: {watch3.color}, {watch3.brand}, Digital: {watch3.is_digital}")

# Calling the method
watch1.ticking()
watch2.ticking()
watch3.ticking()

#Inheritance and Polymorphism
class Watch:
    def __init__(self, color, brand, is_digital=True):
        self.color = color
        self.brand = brand
        self.is_digital = is_digital

    def show_time (self):
        raise 

class DigitalWatch(Watch):
    def __init__(self, color, brand):
        super().__init__(color, brand, is_digital=True)
        self.is_digital = True

    def show_time(self):
        print(f"Showing time in digital format")

class AnalogWatch(Watch):
    def __init__(self, color, brand):
        super().__init__(color, brand, is_digital=False)
        self.is_digital = False
    def show_time(self):
        print(f"Showing time in analog format")

my_Digital_watch = DigitalWatch("black", "Rolex")
my_Analog_watch = AnalogWatch("silver", "Casio")
watches = [my_Digital_watch, my_Analog_watch]
for watch in watches:
    print(f"Watch Color: {watch.color}, Brand: {watch.brand}, Is Digital: {watch.is_digital}")
    watch.show_time()