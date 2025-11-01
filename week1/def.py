#def is way to create functions in python

def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)

#alternative way
def hello1(to):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello1(name)

# Another alternative way
# Create our own function
def hello2(to="world"):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello2(name)

# Output without passing the expected arguments
hello2()

# Another alternative way
def main():

    # Output using our own function
    name = input("What's your name? ")
    hello3(name)

    # Output without passing the expected arguments
    hello3()


# Create our own function
def hello3(to="world"):
    print("hello,", to)