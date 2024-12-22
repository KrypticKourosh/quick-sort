import quick_sort
import random

def main():
    array = [random.randint(1, 100) for _ in range(10)]
    print(f"unsorted array: {array}")
    quick_sort.quick_sort(array, 0, len(array) - 1)
    print(f"sorted array: {array}")

if __name__ == "__main__":
    main()
