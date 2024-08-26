def calc(x, valor):
    return (x - 1) * valor

achei = False
for val in (range(200)):
    for pair in ([2, 16], [3, 32], [4, 48]):
        if calc(pair[0], val+1) == pair[1]:
            print(f"Achei uma correspondência: {val+1} {pair}")
            achei = True

if not achei:
    print("Damn...")
