class car:
    def __init__(self, brand, model, color, fuel):
        self.brand = brand
        self.model = model
        self.color = color
        self.fuel = fuel

        self.started = False
        self.speed = 0

    def start(self):
        if self.started:
            print("the car is already started, nothing else happens")
        else:
            print(f"{self.model} car")
            self.started = True

    def turn_off(self):
        if self.started:
            print("turn off car")
            self.car = False
        else:
            print("the car is already turn off, nothing else happens")
            self.started = True

    def speed_up(self):
        if self.started:
            self.speed += 1
            print(f"{self.speed}km/h")
        else:
            print("can't accelerate, car off")

    def brake(self):
        if self.started:
            self.speed -= 1
            print(f"{self.speed}km/h")
        else:
            print("can't brake, car off")