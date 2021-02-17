def bubble_sort(array):
    for q in range(len(array)):
        has_swapped = False

        for w in range(len(array) - q - 1):
            if array[w] > array[w + 1]:
                array[w], array[w + 1] = array[w + 1], array[w]
                has_swapped = True

        if not has_swapped:
            break


def main():
    array = [int(q) for q in input().split()]
    bubble_sort(array)
    print(*array)


if __name__ == "__main__":
    main()
