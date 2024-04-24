# William Romine
# 00103649
# Dr. Lewis CS472
# https://www.geeksforgeeks.org/radix-sort/
# https://www.programiz.com/dsa/radix-sort

def count_sort(arr, digit):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = arr[i] // digit
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = arr[i] // digit
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]

def radix_sort(arr):
    max_element = max(arr)
    digit = 1
    while max_element // digit > 0:
        count_sort(arr, digit)
        digit *= 10

data = [101, 739, 222, 956, 493, 567, 890, 345, 631, 910]
radix_sort(data)
print(data)