from tire import Tire


class OctoprimeTire():
    def __init__(self, tire_worn):
        self.tire_worn = tire_worn

    def needs_service(self):
        return sum(self.tire_worn) >= 3
