# William Romine
# 00103649
# Dr. Lewis CS472
# https://www.geeksforgeeks.org/python-program-for-binary-insertion-sort/

def insertion_sort(arr):
    for current_index in range(1, len(arr)):
        key = arr[current_index]
        shift_index = current_index - 1
        while shift_index >= 0 and arr[shift_index] > key:
            arr[shift_index + 1] = arr[shift_index]
            shift_index -= 1
        arr[shift_index + 1] = key
    return arr

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1

def binary_insertion_sort(arr):
    for current_index in range(1, len(arr)):
        key = arr[current_index]
        idx = binary_search(arr[:current_index], key)
        if idx != -1:
            arr = arr[:idx] + [key] + arr[idx:]
    return arr

def main():
    arr = [10, 15, 12, 3, 7]
    print("Original Array:", arr)
    sorted_arr = insertion_sort(arr)
    print("Array in Insertion Sort:", sorted_arr)
    sorted_arr = binary_insertion_sort(arr)
    print("Array in Binary Insertion Sort:", sorted_arr)

if __name__ == "__main__":
    main()