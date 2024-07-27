
def whats_the_point(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            print("Not a point")

if __name__ == "__main__":
    point_list = [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2)]
    for point in point_list:
        print(point, end=" ")
        whats_the_point(point)
