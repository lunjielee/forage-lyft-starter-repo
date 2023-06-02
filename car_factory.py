from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(capulet_engine(current_mileage, last_service_mileage), spindler_battery(current_date, last_service_date))

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(willoughby_engine(current_mileage, last_service_mileage), spindler_battery(current_date, last_service_date))

    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car(sternman_engine(warning_light_on), spindler_battery(current_date, last_service_date))

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(willoughby_engine(current_mileage, last_service_mileage), nubbin_battery(current_date, last_service_date))

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(capulet_engine(current_mileage, last_service_mileage), nubbin_battery(current_date, last_service_date))
