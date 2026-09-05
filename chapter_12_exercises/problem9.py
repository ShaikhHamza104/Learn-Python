"""
📚 Topic: Problem9

This script demonstrates problem9 using user input, conditions, functions
and classes.

💡 Key points:
    1️⃣ the basic syntax for problem9
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem9 affects the result.
"""


# Define TemperatureError with a message and temperature. Raise it when the
# temperature is below -273.15 degrees (absolute zero).


class TemperatureError(Exception):
    def __init__(self, m, temp):
        self.massage = m
        self.temperature = temp


def takeTemperature(temp):
    if temp <= -273.14:
        raise TemperatureError("Temprature must be grater then -273.15", temp)


try:
    temp = float(input("Enter temperature: "))
    takeTemperature(temp)

except TemperatureError as e:
    print(e)

except ValueError:
    print("You are entering non digits numbers")
