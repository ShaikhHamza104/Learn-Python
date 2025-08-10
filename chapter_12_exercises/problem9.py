# 9: Define a custom exception class TemperatureError with a constructor that takes a message and a temperature value. Write a function that raises this exception if the temperature is below -273.15 (absolute zero).

class TemperatureError(Exception):
    def __init__(self,m,temp):
        self.massage=m
        self.temperature=temp
    
def takeTemperature(temp):
    if temp<=-273.14:
        raise TemperatureError("Temprature must be grater then -273.15",temp)
    
try:
    temp=float(input("Enter temperature: "))
    takeTemperature(temp)

except TemperatureError as e:
    print(e)

except ValueError as e:
    print("You are entering non digits numbers")