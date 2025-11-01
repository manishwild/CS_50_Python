x = input("What's x? ")
y = input("What's y? ")

# Convert x and y to integers and add them
z = int(x) + int(y)

print(z)
#alternative way
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
# Alternative way using map to convert inputs to integers
x, y = map(int, (input("What's x? "), input("What's y? ")))
print(x + y)