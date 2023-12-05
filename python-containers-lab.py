# Python Containers Lab


# Exercise 1

print("Exercise 1")
print("=======================")


# Solution Here

students = ["Ben", "Nathanael", "Henry", "Ed"]

print(students, "<-- students")
print("-----")
print(students[1], "<-- students[1]")
print(students[-1], "<-- students[-1]")

print("")



# Exercise 2

print("Exercise 2")
print("=======================")


# Solution Here

foods = ("sushi", "curry", "ramen", "pho")
print(foods, "<-- foods")

print("-----")

for food in foods:
    print(f"{food.capitalize()} is a good food!")

print("")



# Exercise 3

print("Exercise 3")
print("=======================")


# Solution Here

for food in foods[-2:]:
    print(f"{food.capitalize()} is one of the last two foods!")

print("")



# Exercise 4

print("Exercise 4")
print("=======================")


# Solution Here

home_town = {
    "city": "New York City",
    "state": "New York",
    "population": "8.468 million"
}

print(f"I was born in ${home_town['city']}, {home_town['state']} - population of {home_town['population']}!")

print("")



# Exercise 5

print("Exercise 5")
print("=======================")


# Solution Here

for key, value in home_town.items():
    print(f"Ben's home town's {key} is {value}!")

print("")



# Exercise 6

print("Exercise 6")
print("=======================")


# Solution Here

cohort = []

for idx, student in enumerate(students):
    cohort.append(
        {
            "student": student,
            "fav_food": foods[idx]
        }
    )

for person in cohort:
    print(f"{person['student'].capitalize()}'s favorite food is {person['fav_food'].lower()}!")

print("")



# Exercise 7

print("Exercise 7")
print("=======================")


# Solution Here

awesome_students = [f"{student.capitalize()} is awesome!" for student in students]
print(awesome_students, "<-- awesome_students")

print("-----")

for awesome_student in awesome_students:
    print(awesome_student)

print("")



# Exercise 8

print("Exercise 8")
print("=======================")


# Solution Here

for contains_a in [food for food in foods if food.__contains__("a")]:
    print(f'{contains_a.capitalize()} is a food in the foods list that contains the letter "a".')


        

