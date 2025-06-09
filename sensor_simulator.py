import random

class SensorSimulator:
    def __init__(self):
        self.value = 0

    def read_value(self):
        # Simuliere Temperatur zwischen 60 und 100 °C
        self.value = random.uniform(60, 100)
        return self.value
    