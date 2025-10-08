# Function to compare two numbers
def greater_than(x, y):
    if x > y:
        return True
    else:
        return False

# Main program
a = 2
b = 3

# Call the function and store the result
result = greater_than(a, b)

# Print the result
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))

# --- Test with new values ---
a = 10
b = 6

result = greater_than(a, b)
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
