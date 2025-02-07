from abc import ABC, abstractmethod
from serviceable import Serviceable
from engine import Engine
from battery import Battery


class Car(Engine, Battery, Serviceable, ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service():
            return True
