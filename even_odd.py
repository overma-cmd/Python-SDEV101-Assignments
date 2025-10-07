# Program to check if numbers in a list are even or odd
# Author: Oasheen Verma
# Date: October 7, 2025
# Description: This program creates a list of 15 numbers and uses a loop  to determine if each number is even or odd.

# Create a list of 15 numbers
numbers = [1, 4, 7, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42]

# Loop through each number in the list
for number in numbers:
    # Check if the number is even
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
