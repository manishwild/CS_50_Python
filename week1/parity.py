# % remainder operator
x = int(input("What's x? "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")


#creating a function
def main():
        y = int(input("What's y? "))
        if is_even(y):
            print("Even")
        else:
            print("Odd")  

def is_even(n):
        if n % 2 == 0:
            return True 
        else:
            return False
main()