import time
from sensortemp import TemperatureSensor
from servicelogger import LoggerService
from util import TemperatureStats


sensor = TemperatureSensor()
logger = LoggerService("data.csv")
stats = TemperatureStats()

print("Temperature Logger Started...\n")

while True:

    temperature = sensor.read_temperature()

    logger.log(temperature)
    stats.add(temperature)

    print("Current Temperature:", temperature, "°C")
    print("Max Temperature:", stats.get_max(), "°C")
    print("Min Temperature:", stats.get_min(), "°C")
    print("Average Temperature:", stats.get_average(), "°C")

    print("--------------------------------")

    time.sleep(3)