# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result and round
z = round(x / y, 2)

# Print the result
print(z)

# Another alternative way
x = float(input("What's x? "))  
y = float(input("What's y? "))

# calculate the result 
z = x / y

# Print the result
print(f"{z:.2f}")