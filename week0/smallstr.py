# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name=input("What is your name? ").strip().title()
# Greet the user with their name
print(f"Hello, {name}!")