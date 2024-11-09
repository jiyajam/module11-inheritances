################1

class Publication:
    def __init__(self, name):
        self.name = name



class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count


    def print_information(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")



class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor


    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")



magazine = Magazine("Donald Duck", "Aki Hyyppä")
magazine.print_information()

print()


book = Book("Compartment No. 6", "Rosa Liksom", 192)
book.print_information()

################2
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed


    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

    def print_info(self):
        print(f"Electric Car {self.registration_number}: {self.max_speed} km/h, {self.battery_capacity} kWh battery, {self.travelled_distance} km travelled")


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, fuel_tank_volume):
        super().__init__(registration_number, max_speed)
        self.fuel_tank_volume = fuel_tank_volume

    def print_info(self):
        print(f"Gasoline Car {self.registration_number}: {self.max_speed} km/h, {self.fuel_tank_volume} L fuel tank, {self.travelled_distance} km travelled")


electric_car = ElectricCar("ABC-15", 180, 52.5)
electric_car.drive(3)
electric_car.print_info()


gasoline_car = GasolineCar("ACD-123", 165, 32.3)
gasoline_car.accelerate(20)
gasoline_car.drive(3)
gasoline_car.print_info()
