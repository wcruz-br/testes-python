# read an integer from STDIN
n = input("Enter a number: ")
if n.isnumeric():
    n = int(n)
    if n < 1 or n > 20:
        print("The number must be between 1 and 20")
    else:
        for i in range(0, n):
            print (i**2)
else:
    print("Please enter only numbers.")
