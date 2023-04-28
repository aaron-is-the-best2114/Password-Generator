import random
import string

def generate_password(length, complexity):
    # Define the complexity options
    if complexity == "easy":
        chars = string.ascii_letters + string.digits
    elif complexity == "medium":
        chars = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "hard":
        chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    
    # Generate the password
    password = "".join(random.choice(chars) for i in range(length))
    
    return password

# Example usage
password_length = int(input("Please Input Password Length: "))
password_complexity = input("Please input Password Complexity: Easy, Medium, Hard: ")
password = generate_password(password_length, password_complexity)
print(password)
