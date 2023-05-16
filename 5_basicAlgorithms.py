# Python Tutorial - Basic Algorithms


'''
    Linear Search:
        Linear search is a simple search algorithm that iterates through a list of elements until it finds the desired value or reaches the end of the list.
'''

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1



'''
    Binary Search:
        Binary search is a more efficient search algorithm for sorted lists.
        It works by repeatedly dividing the search interval in half until the target value is found or the interval becomes empty.
'''
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

'''
    Bubble Sort:
        Bubble sort is a simple sorting algorithm that repeatedly steps through the list, 
        compares adjacent elements and swaps them if they are in the wrong order.
'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

'''
    Quick Sort:
        Quick sort is a divide-and-conquer sorting algorithm that works by partitioning the list into two sub-lists, 
        according to a pivot element, and recursively sorting each sub-list.
'''
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left = [x for x in lst[1:] if x <= pivot]
    right = [x for x in lst[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    selection = input('Select an example of basic algorithm (1) Linear Search (2) Binary Search (3) Bubble Sort (4) Quick Sort: ')

    print('=' * 60)
    if selection == '1':
        my_list = [5, 3, 8, 4, 2]
        target_value = 8
        print('my_list: ', my_list, ', targer_value: ', target_value)
        index = linear_search(my_list, target_value)
        if index != -1:
            print("Element found at index: ", index)
        else:
            print("Element not found!")
    
    elif selection == '2':
        my_list = [2, 4, 8, 12, 16, 20]
        target_value = 12
        print('my_list: ', my_list, ', targer_value: ', target_value)
        index = binary_search(my_list, target_value)
        if index != -1:
            print("Element found at index: ", index)
        else:
            print("Element not found!")
    
    elif selection == '3':
        my_list = [5, 3, 8, 4, 2]
        print("Original list: ", my_list)
        my_list = bubble_sort(my_list)
        print("Sorted list: ", my_list)

    elif selection == '4':
        my_list = [5, 3, 8, 4, 2, 13, 1, 20, 16, 14, 21]
        print("Original list: ", my_list)
        my_list = quick_sort(my_list)
        print("Sorted list: ", my_list)
    else:
        print('Invalid input!')
    print('=' * 60)

