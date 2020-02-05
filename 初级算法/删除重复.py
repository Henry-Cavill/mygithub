def removeDuplicates(nums):
    for i in range(len(nums)):
        j = i + 1
        while j < len(nums) and nums[i] == nums[j]:
            nums.pop(j)
    return nums

    pass


if __name__ == '__main__':
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    num = [1, 1, 2]
    result = removeDuplicates(num)
    print(result)
