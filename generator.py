# Import the random module
import random

# Create a password generator function
def password_generator(length, number):
    # Create a list of characters
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', ':', ';', '"', '<', '>', ',', '.', '?', '/', '`', '~', ' ']
    # Create a list of numbers
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Create a list of special characters
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', ':', ';', '"', '<', '>', ',', '.', '?', '/', '`', '~', ' ']
    # Create a list of passwords
    passwords = []
    # Create a variable to hold the password
    password = ''

    # Loop through the number of passwords
    for i in range(number):
        # Loop through the length of the password
        for j in range(length):
            # Generate a random number
            random_number = random.randint(0, len(characters) - 1)
            # Add the random number to the password
            password += characters[random_number]
        # Add the password to the list of passwords
        passwords.append(password)
        # Reset the password
        password = ''
    # Return the list of passwords
    return passwords

# Create a function to print the passwords
def print_passwords(passwords):
    # Loop through the passwords
    for password in passwords:
        # Print the password
        print(password)

# Get user input so we can generate the passwords
length = int(input('Enter the length of the password: '))
number = int(input('Enter the number of passwords: '))

# Get the passwords
generated = password_generator(length, number)

# Print the passwords
print_passwords(generated)
