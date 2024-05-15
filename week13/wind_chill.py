print("\nWelcome to the wind chill calculator")
temp = ""
while type(temp) != type(4.23):
    try:
        temp = float(input("What is the temperature? "))
    except:
        print("please input an valid number")

temp_type = ""
while temp_type not in ["F", "C"]:
    temp_type = input("Fahrenheit or Celsius (F/C)? ").upper()

if temp_type == "C":
    temp = temp * 9 / 5 + 32

def calculate_wind_chill(T, V):
    return 35.74 + 0.6214 * T - 35.75 * V ** 0.16 + 0.4275 * T * V ** 0.16

for velocity in range(5, 65, 5):
    print(f"At temperature {temp}F, and wind speed {velocity} mph, the windchill is: {calculate_wind_chill(temp, velocity):.02f}F")

print()