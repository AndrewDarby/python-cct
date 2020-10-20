x = -1 # Initialize a variable to use in the condition

while x < 10:
    x += 1
    if ((x % 2) == 0): # If the number is even
        print(x)

valid_input = False # Used to mark if input is valid

while not valid_input: # Loop when valid input is False
  number = int(input("Please type a number between 1 and 10: ")) # Take user input

  if number < 1: # Number is too small
    print("Number provided is less than 1")

  if number > 10: # Number is too large
    print("Number provided is greater than 10")

  else: # If the input is in a valid range
    valid_input = True # End the loop
    