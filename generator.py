# Import the sys module
import sys
# import the random module
import random
# Import the random module
import string

# Create password generator function
def password_generator(length, number):
    # Create a list to hold the passwords
    passwords = []
    # Loop through the number of passwords
    for i in range(number):
        # Create a variable to hold the password
        password = ''
        # Loop through the length of the password
        for i in range(length):
            # Add a random character to the password
            password += random.choice(string.ascii_letters + string.digits)
        # Add the password to the list
        passwords.append(password)
    # Return the list of passwords
    return passwords

# Create function to print the passwords
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
