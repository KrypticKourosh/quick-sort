def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
    (array[high], array[i + 1]) = (array[i + 1], array[high])
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)