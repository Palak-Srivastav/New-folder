import random

class TemperatureSensor:

    def read_temperature(self):
        # simulate temperature between 20°C and 40°C
        return round(random.uniform(20, 40), 2)