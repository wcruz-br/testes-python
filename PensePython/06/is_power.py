def is_power(a, b):
    if a == 0 or b == 0:
        return False
    if a == 1:
        return True
    return (a % b == 0) and is_power(a/b, b)

print(is_power(3,2))
print(is_power(0, 438934))
print(is_power(2139879343472,2))
print(is_power(999, 3))
print(is_power(8, 2))
print(is_power(65536, 2))
print(is_power(1,30))
print(is_power(8, 2))
