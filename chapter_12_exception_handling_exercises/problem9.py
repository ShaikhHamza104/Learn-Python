"""
📚 Topic: Chapter 12 Exercise - Problem 9

Define a custom `TemperatureError` for values below absolute zero (-273.15 C).

💡 Key points:
    1️⃣ Custom exception storing error message and temperature value
    2️⃣ Raising on inputs below absolute zero
    3️⃣ Formatting descriptive error messages
"""


# Define TemperatureError with a message and temperature. Raise it when the
# temperature is below -273.15 degrees (absolute zero).


class TemperatureError(Exception):
    def __init__(self, message, temp):
        super().__init__(message)
        self.message = message
        self.temperature = temp

    def __str__(self):
        return f"{self.message} (received: {self.temperature})"


def take_temperature(temp):
    if temp < -273.15:
        raise TemperatureError(
            "Temperature must be greater than or equal to -273.15", temp
        )


try:
    temp = float(input("Enter temperature: "))
    take_temperature(temp)

except TemperatureError as e:
    print(e)

except ValueError:
    print("You are entering non digits numbers")
