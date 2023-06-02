from car import Car
from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine
from battery import nubbin_battery
from battery import spindler_battery


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
