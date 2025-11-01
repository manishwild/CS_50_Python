# Ask the user for their name and store it in a variable
name=input("What is your name? ")
# remove whitespace from the string
name=name.strip() 
# Capitalize the first letter of each word
name=name.title()
# Greet the user with their name
print(f"Hello, {name}!")