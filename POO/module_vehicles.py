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

class furgo(vehicle):
    
    def load(self,loading):
        self.loaded=loading
        if (self.loaded):
            return "The furgo is loaded"
        else:
            return "The furgo is empty"


class motorbike(vehicle):
    up_wheels=""

    def turning_up_wheels(self):
        self.up_wheels="I'm turning up the wheels"

    def status(self):
        print(self.brand,self.model,self.accelerate,self.brakes,self.ongoing,self.up_wheels)

class electric_v(vehicle):
    def __init__(self,brand,model):
        super().__init__(brand,model)
        self.autonomy=100

    def energy_charging(self):
        self.energy_charging=True

class electric_bike(electric_v,vehicle):
    pass