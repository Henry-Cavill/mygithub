def partition(list, left, right):
    mid = list[left]
    while left < right:
        while list[right] >= mid and left < right:
            right -= 1
        list[left] = list[right]
        while list[left] <= mid and left < right:
            left += 1
        list[right] = list[left]
    list[left] = mid
    return left


if __name__ == '__main__':
    list = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    left = 0
    right = len(list) - 1
    # partition(list, left, right)
    print(sorted(list))
    # print(list)
