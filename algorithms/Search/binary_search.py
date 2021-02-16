def binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        middle = (left + right) // 2

        if array[middle] == target:
            return middle
        elif target < array[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return -1


def main():
    target = int(input())
    array = [int(q) for q in input().split()]
    print(binary_search(array, target))


if __name__ == "__main__":
    main()
