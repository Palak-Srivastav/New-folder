import csv
from datetime import datetime

class LoggerService:

    def __init__(self, filepath):
        self.filepath = filepath

    def log(self, temperature):

        with open(self.filepath, "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                temperature
            ])