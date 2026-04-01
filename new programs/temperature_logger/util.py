class TemperatureStats:

    def __init__(self):
        self.temperatures = []

    def add(self, temp):
        self.temperatures.append(temp)

    def get_max(self):
        return max(self.temperatures)

    def get_min(self):
        return min(self.temperatures)

    def get_average(self):
        return round(sum(self.temperatures) / len(self.temperatures), 2)