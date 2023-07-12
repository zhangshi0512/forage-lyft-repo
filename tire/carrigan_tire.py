from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        return any(tire_wear >= 0.9 for tire_wear in self.tire_wear_array)
