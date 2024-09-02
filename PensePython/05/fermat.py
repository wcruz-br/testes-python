def check_fermat(a, b, c, n):
    print(f"{a}**{n} + {b}**{n} == {c}**{n}")
    print(f"{a**n} + {b**n} == {c**n}")
    print(f"{a**n + b**n} == {c**n}")
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")
    print("")

def ask_for_numbers():
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    n = int(input("n:"))
    check_fermat(a, b, c, n)

def test_fermat():
    for a in range(1,201):
        for b in range(1,201):
            for c in range(1,201):
                for n in range(2,21):
                    if n > 2 and a**n + b**n == c**n:
                        print("")
                        print("Holy smokes, Fermat was wrong!")
                        print(f"{a}**{n} + {b}**{n} == {c}**{n}")
                        print(f"{a**n} + {b**n} == {c**n}")
                        print(f"{a**n + b**n} == {c**n}")
                        print("")
                    else:
                        if b == c == n == 20:
                            print(a, end=" ")

if __name__ == "__main__":
     ask_for_numbers()
     # test_fermat()
