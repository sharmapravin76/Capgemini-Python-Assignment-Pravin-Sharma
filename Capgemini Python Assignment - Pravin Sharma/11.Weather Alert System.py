# Weather Alert System

temperature = float(input("Enter the temperature in °C: "))

if temperature > 40:
    print("Heat Alert")
elif 30 < temperature <= 40:
    print("Warm")
else:
    print("Normal")