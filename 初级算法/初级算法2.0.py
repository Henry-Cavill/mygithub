def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            nums[i + 1] = nums[j]
            i += 1
    return i + 1


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = removeDuplicates(nums)
    print(result)
