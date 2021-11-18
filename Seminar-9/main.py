def binarysearchrecursive(sequence, x, left, right):
    if left > right:
        return False
    mid = (left + right) // 2
    print('mid', sequence[mid])

    if x == sequence[mid]:
        return mid
    elif x < sequence[mid]:
        return binarysearchrecursive(sequence, x, left, mid - 1)
    elif x > sequence[mid]:
        return binarysearchrecursive(sequence, x, mid + 1, right)


if __name__ == "__main__":
    sample = [1, 2, 5, 6, 8, 10, 50, 70, 75, 77, 78, 79, 80, 81, 82, 85]
    x = 77
    print('Index of number ', x, 'is equal to ', binarysearchrecursive(sample, x, 0, len(sample) - 1))