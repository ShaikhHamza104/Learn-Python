# 2. Write a python program using function to convert Celsius to Fahrenheit.
# F=(9/5)C+32


def celsiusToFahrenheit(f):
    
    return 5*(f-32)/9
f=int(input("Enter temperature in F : "))
print(f"Fahrenheit {f} to celsius  is {round(celsiusToFahrenheit(f),2)}")