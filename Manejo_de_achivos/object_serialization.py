import pickle

class vehicle():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.ongoing=False
        self.accelerate=False
        self.brakes=False

    def start_going(self):
        self.ongoing=True

    def slowing_down(self):
        self.brakes=True

    def speeding_up(self):
        self.accelerate=True

    def status(self):
        print(self.brand,self.model,self.accelerate,self.brakes,self.ongoing)

car1=vehicle("Mazda","MX5")
car2=vehicle("Seat","Leon")
car3=vehicle("Renault","Megane")

cars=[car1,car2,car3]

archive=open("The Cars","wb")
pickle.dump(cars,archive)
archive.close()
del archive

archive_opening=open("The Cars","rb")
my_cars=pickle.load(archive_opening)
archive_opening.close()

for c in my_cars:
    print(c.status())