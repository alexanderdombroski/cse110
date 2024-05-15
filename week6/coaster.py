age1 = int(input("What is the age of the first rider? "))
height1 = int(input("What is the height of the first rider? "))
rider2 = input("Is there a second rider (yes/no)? ").lower()
age2 = 16
height2 = 60
rideable = False

if rider2 == "yes":
    age2 = int(input("What is the age of the second rider? "))
    height2 = int(input("What is the height of the second rider? "))

golden_ticket = "no"
if age1 < 18 and age2 < 18 and age1 >=12 and age2 >= 12:
    golden_ticket = input("Do you have a golden passport? (yes/no) ").lower()
if golden_ticket == "yes":
    age1 = 18
    age2 = 18

if age1 >= 18 and height1 >= 62 or\
    age2 >= 18 and height2 >= 62:
    rideable = True
elif age1 >= 12 and height1 >= 52 and\
    age2 >= 12 and height2 >= 52:
    rideable = True
elif age1 >= 16 and age2 >= 14 or\
    age1 >= 14 and age2 >= 16:
    rideable = True

if height1 < 36 or height2 < 36:
    rideable = False


if rideable:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")