def merge(left_array, right_array):
    left_length, right_length = len(left_array), len(right_array)
    left_index, right_index = 0, 0
    sorted_array = []

    while left_index < left_length and right_index < right_length:
        if left_array[left_index] <= right_array[right_index]:
            sorted_array.append(left_array[left_index])
            left_index += 1
        else:
            sorted_array.append(right_array[right_index])
            right_index += 1

    if left_index == left_length:
        sorted_array.extend(right_array[right_index:])
    else:
        sorted_array.extend(left_array[left_index:])

    return sorted_array


def merge_sort(array):
    if len(array) < 2:
        return array

    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(left, right)


def main():
    array = [int(q) for q in input().split()]
    print(*merge_sort(array))


if __name__ == "__main__":
    main()
