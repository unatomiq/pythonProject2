import random


def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle - 1] < element <= array[middle]:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


while True:
    str_arr = input("Введите последовательность чисел: ")
    try:
        arr = list(map(int, str_arr.split(' ')))
        break
    except ValueError as e:
        print(e)

while True:
    str_elem = input("Введите число: ")
    try:
        elem = int(str_elem)
        break
    except ValueError as e:
        print(e)

qsort_random(arr, 0, len(arr) - 1)
result = binary_search(arr, elem, 0, len(arr) - 1)

if result is False:
    print('Элемент не найден')
else:
    print(f'Номер позиции элемента: {result}')
