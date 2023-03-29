class car():

    def __init__(self):
        self.__chasis_long=900
        self.__chasis_wide=400
        self.__car_wheels=4
        self.__ongoing=False
    

    def start_up(self,start):
        self.__ongoing=start

        if (self.__ongoing):
            check1=self.__check()

        if(self.__ongoing and check1):
            return "My car is running"
        elif(self.__ongoing and check1==False):
            return "Something went wrong, can't strat running"
        else:
            return "My car is stopped"
            

    def status(self):
        print(my_car.__chasis_long,my_car.__chasis_wide,my_car.__car_wheels)

    def __check(self):
        print("Doing internal check")
        self.oil="ok"
        self.gas="ok"
        #self.gas="low"
        self.doors="Close"
        if (self.oil=="ok" and self.gas=="ok" and self.doors=="Close"):
            return True
        else:
            return False


my_car=car()
print(my_car.start_up(True))
my_car.status()

#in the next lines the second object is created

my_car2=car()
print(my_car.start_up(False))
my_car2.status()
