print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    if age >= 18:
        print("Your cost will be $12 to ride.")
    elif age < 18:
        print("Your cost will be $7 to ride.")
else:
    print("Sorry you have to grow taller before you can ride.")
