# Base Class for Devices
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        return f"{self.brand} {self.model} is powering on!"

    def power_off(self):
        return f"{self.brand} {self.model} is shutting down."


# Derived Class for Smartphones
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_resolution):
        super().__init__(brand, model)
        self.storage = storage
        self.camera_resolution = camera_resolution

    def take_photo(self):
        return f"{self.brand} {self.model} is taking a photo with its {self.camera_resolution} MP camera."

    def install_app(self, app_name):
        return f"{app_name} is being installed on {self.brand} {self.model}."


# Base Class for Animals
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Derived Classes for Animals
class Dog(Animal):
    def move(self):
        return "Running on four legs 🐕."


class Bird(Animal):
    def move(self):
        return "Flying through the sky 🐦."


class Fish(Animal):
    def move(self):
        return "Swimming in water 🐟."


# Polymorphism Demonstration
def animal_moves(animal):
    print(animal.move())


# Main Execution
if __name__ == "__main__":
    # Smartphone Example
    phone = Smartphone("Apple", "iPhone 14", "256GB", "12")
    print(phone.power_on())
    print(phone.take_photo())
    print(phone.install_app("Instagram"))
    print(phone.power_off())

    # Polymorphism Example with Animals
    dog = Dog()
    bird = Bird()
    fish = Fish()

    animal_moves(dog)   # Output: Running on four legs 🐕.
    animal_moves(bird)  # Output: Flying through the sky 🐦.
    animal_moves(fish)  # Output: Swimming in water 🐟.
