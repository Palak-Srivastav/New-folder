from abc import ABC, abstractmethod

# -------------------------------
# 1️⃣ Abstraction
# -------------------------------
class Sensor(ABC):
    
    @abstractmethod
    def read_data(self):
        pass


# -------------------------------
# 2️⃣ Encapsulation
# -------------------------------
class UltrasonicSensor(Sensor):
    
    def __init__(self, distance):
        self.__distance = distance   # private variable

    def read_data(self):
        return f"Ultrasonic distance: {self.__distance} cm"

    def set_distance(self, value):
        self.__distance = value


class SoilMoistureSensor(Sensor):
    
    def __init__(self, moisture):
        self.__moisture = moisture

    def read_data(self):
        return f"Soil moisture: {self.__moisture} %"

    def set_moisture(self, value):
        self.__moisture = value


# -------------------------------
# 3️⃣ Inheritance
# -------------------------------
class SmartSensor(UltrasonicSensor):

    def alert(self):
        data = self.read_data()
        print("Checking obstacle...")
        print(data)


# -------------------------------
# 4️⃣ Polymorphism
# -------------------------------
def display_sensor_data(sensor):
    print(sensor.read_data())


# -------------------------------
# Main Program
# -------------------------------

ultra = UltrasonicSensor(50)
soil = SoilMoistureSensor(45)

smart = SmartSensor(20)

display_sensor_data(ultra)
display_sensor_data(soil)

smart.alert()