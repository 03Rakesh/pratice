import random
import string

def generate_random_password(length=12):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Generate and print a random password
random_password = generate_random_password()
print("Generated Password:", random_password)
