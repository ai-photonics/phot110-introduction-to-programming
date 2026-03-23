class Vehicle:
    """ Transport of vehicles between locations """

    def __init__(self, location):
        self.cities = ["Izmir", "Bursa", "Paris"]
        if location in self.cities:
            self.location = location
        else:
            raise Exception

    def drive_to_city(self, city):
        print(f"Drive from {self.location} to {city}")
        self.location = city
        ...

class Truck(Vehicle):
    """ Truck extends Vehicles with a cargo """

    def __init__(self, location, cargo):
        super().__init__(location)
        self.cargo = cargo


class Bus(Vehicle):
    """ Bus extends Vehicles with accepting passengers if the bus is not full """

    def __init__(self, location, passengers):
        super().__init__(location)
        self.max_passengers = 4
        self.passengers = passengers


class Dolmus(Bus):
    """ Dolmus extends Bus by having a limited gasoline tank """
    def __init__(self, location, passengers, gasoline):
        super().__init__(location, passengers)
        self.gasoline = gasoline

    def take_gasoline(self, liters):
        self.gasoline = self.gasoline + liters

    ...


def test_vehicle_class():
    """ Verifying whether the Vehicle class works as expected """
    car = Vehicle("Izmir")
    print(car.location)
    print(car.cities)
    car.drive_to_city("Paris")

def test_truck_class():
    """ Testing the Truck class, and checking whether the initial location is verified """
    try:
        truck = Truck("Izmir", ["box with scrolls"])
        print(truck.location)
        print(truck.cargo)
        truck.drive_to_city("Bursa")
    except Exception:
        pass


def test_wrong_location():
    """ Testing the Bus class, and filling the wrong initial location: should not work. """
    try:
        bus = Bus("Izmire", ["Kemal", "Bob"])
        bus.drive_to_city("Paris")
    except:
        pass

def test_subsubclass():
    """ Showcases a derived class from the derived Bus class. """
    dolmus1 = Dolmus("Paris", ["Zeynep"], 34)
    dolmus1.drive_to_city("Bursa")


# Performing the different functions that show the
# working of classes and subclasses
# Comment out one by one to see what each function does.
test_vehicle_class()
test_truck_class()
test_wrong_location()
test_subsubclass()
