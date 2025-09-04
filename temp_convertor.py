# Author: Vedant Naik
# Date: 09/04/2025
# Fahrenheit <-> Celsius Converter

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Temperature Converter")
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")

number = input("Choose option 1 or 2:   ")

if number == "1":
    c = float(input("Enter temperature in Celsius: "))
    print(f"{c} °C = {celsius_to_fahrenheit(c):.2f} °F")
elif number == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    print(f"{f} °F = {fahrenheit_to_celsius(f):.2f} °C")
else:
    print("Invalid choice.")
