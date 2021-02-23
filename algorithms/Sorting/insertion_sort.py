def insertion_sort(array):
    for q in range(len(array)):
        key = array[q]
        w = q - 1 

        while array[w] > key and w >= 0:
            array[w + 1] = array[w]
            w -= 1

        array[w + 1] = key


def main():
    array = [int(q) for q in input().split()]
    insertion_sort(array)
    print(*array)


if __name__ == "__main__":
    main()
