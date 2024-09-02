def is_triangle(a, b, c):
    if  a > b + c   or  b > a + c   or  c > a + b:
        print("No")
    else:
        print("Yes")

def ask_for_numbers():
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    is_triangle(a, b, c)

if __name__ == "__main__":
    ask_for_numbers()
