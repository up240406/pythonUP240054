#     LEVEL 2
#1.-   Grade students based on their scores
score = int(input("Enter your score: "))

if 80 <= score <= 100:
    grade = "A"
elif 70 <= score < 80:
    grade = "B"
elif 60 <= score < 70:
    grade = "C"
elif 50 <= score < 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

#2.-   Check the season based on user input
month = input("Enter the month: ").strip().capitalize()

if month in ["September", "October", "November"]:
    season = "Autumn"
elif month in ["December", "January", "February"]:
    season = "Winter"
elif month in ["March", "April", "May"]:
    season = "Spring"
elif month in ["June", "July", "August"]:
    season = "Summer"
else:
    season = "Invalid month"

print(f"The season is: {season}")

#3.-   Check if a fruit exists in the list, if not add it
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_to_add = input("Enter a fruit: ").strip().lower()

if fruit_to_add in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit_to_add)
    print("Updated fruit list:", fruits)