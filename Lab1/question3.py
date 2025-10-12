# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

from datetime import datetime

name = input("Enter Your Name :")
age = int(input("Enter Your Age :"))

current_year = datetime.now().year
year_turn_100 = current_year + (100 - age)

print(f"Hello, {name}! You will turn 100 years old in the year {year_turn_100}.")