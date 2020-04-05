class Vehicle():
    def __init__(self,wheel,door):
        self.wheel = wheel
        self.door = door

    def opendoor():
        print("door is opened!")

class Bus(Vehicle):
    def __init__(self,wheels,doors,seats):
        super().__init__(wheels,doors)
        self.seat = seats

    def autodoor():
        print("door is opened!")



bus = Bus(4,2,22)

print(bus.wheel,bus.door,bus.seat)
