def linear_search(array, target):
    for index in range(len(array)):
        if array[index] == target:
            return index

    return -1


def main():
    target = int(input())
    array = [int(q) for q in input().split()]
    print(linear_search(array, target))


if __name__ == "__main__":
    main()
