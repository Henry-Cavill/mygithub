def rotate(nums, k):
    i = 0
    n = len(nums)
    if n == 0:
        return -1
    for i in range(n-k-1):
        nums[i], nums[(i+k) % n] = nums[(i+k) % n], nums[i]
    return nums


if __name__ == '__main__':
    num = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate(num, k))
