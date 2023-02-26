import time
import random
attemps_count = 1
user_input=0
print("Welcome! Do you feel lucky today? Let's check it then :D")
print("Enter a range that you want to pick a number from!")
range_min = int(input("min: "))
range_max = int(input("max: "))
random_number = random.randint(range_min, range_max)
range_difference = range_max - range_min +1
points = 100
while user_input != random_number:
    user_input = int(input("Predict the number: "))

    if user_input > random_number:
        print("Nope, go down :)")
        attemps_count += 1
        points = points - (100 / (range_difference))
        
    elif user_input < random_number:
        print("Nope, go up :)")
        attemps_count += 1
        points = points - (100 / (range_difference))
    else:
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        print("PERFECT!!! YOU ARE SO SMART!!! ;) ")
        
        print("You tried " + str(attemps_count) + " times and found. And your points:" + str(points))
        continue
