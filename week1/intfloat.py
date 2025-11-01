#float
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)
# Alternative way using map to convert inputs to floats
x, y = map(float, (input("What's x? "), input("What's y?")))
# Create a rounded result
z = round(x + y)

# Print the result
print(z)

# Another alternative way
x = float(input("What's x? "))  
y = float(input("What's y? "))

# calculate the result and round it
z = round(x + y,2)
# Print the result
print(z)