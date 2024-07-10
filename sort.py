def bubble_sort(array):
    sorted = False
    array_lenght = len(array)
    while not sorted:
        sorted = True
        for i in range(array_lenght - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
    return array

def counting_sort(array):
    contador = [0] * (max(array) + 1)
    for element in array:
        contador[element] += 1
    saida = []
    for i in range(len(contador)):
        saida.extend([i] * contador[i])
    return saida

def merge_sort(array):
    size = len(array)
    if size < 2:
        return array
    else:
        middle = size // 2
        left_part = merge_sort(array[:middle])
        right_part = merge_sort(array[middle:])
        saida = []
        l = 0
        r = 0
        while l < len(left_part) and r < len(right_part):
            if left_part[l] < right_part[r]:
                saida.append(left_part[l])
                l += 1
            else:
                saida.append(right_part[r])
                r += 1
        while l < len(left_part):
            saida.append(left_part[l])
            l += 1
        while r < len(right_part):
            saida.append(right_part[r])
            r += 1
        return saida

# ------------------------------------------- #

list = [7, 2, 5, 1, 9, 3, 0]
print(bubble_sort(list))

list = [7, 2, 5, 1, 9, 3, 0]
print(counting_sort(list))

list = [7, 2, 5, 1, 9, 3, 0]
print(merge_sort(list))
