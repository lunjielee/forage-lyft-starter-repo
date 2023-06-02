from tire import Tire


class CarriganTire():
    def __init__(self, tire_worn):
        self.tire_worn = tire_worn

    def needs_service(self):
        for i in self.tire_worn:
            if i >= 0.9:
                return True
