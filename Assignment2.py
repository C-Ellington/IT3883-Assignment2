# Program Name: Assignment2.py
# Course: IT3883
# Student Name: Cobyanne Ellington
# Assignment Number: Assignment 2
# Due Date: 10/02/2026
# Purpose: This program reads student scores from a file,
# calculates each average, and displays them from highest to lowest.
# Resources: Course notes and Python textbook

# Stores student results
results = []

# Opens the input file
input_file = open("Assignment2input.txt", "r")

# Reads each student
for line in input_file:
    data = line.split()

    # Gets student name
    name = data[0]

    # Stores the scores
    scores = []

    for score in data[1:]:
        scores.append(int(score))

    # Calculates average
    average = sum(scores) / len(scores)

    # Saves average and name
    results.append((average, name))

# Closes the file
input_file.close()

# Sorts highest to lowest
results.sort(reverse=True)

# Displays results!
for average, name in results:
    print(name, f"{average:.2f}")