class car():

    def displacement(self):
        print("I move using 4 wheels")

class bike():

    def displacement(self):
        print("I move using 2 wheels")

class trunk():

    def displacement(self):
        print("I move using 6 wheels")

def vehicle_displacement(vehicle):
    vehicle.displacement()

my_vehicle1=bike()
vehicle_displacement(my_vehicle1)

my_vehicle2=car()
vehicle_displacement(my_vehicle2)

my_vehicle3=trunk()
vehicle_displacement(my_vehicle3)


