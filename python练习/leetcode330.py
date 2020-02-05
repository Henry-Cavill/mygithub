def minPatches(nums):
    sets = {0}
    for i in range(len(nums)-1):
        sets.add(nums[i])
        for j in range(i+1, len(nums)):
            sets.add(nums[j])
            addnum = nums[i]+nums[j]
            sets.add(addnum)
    for i in sets:
        print(i)


if __name__ == '__main__':
    nums = [1, 5, 10]
    n = 20
    minPatches(nums)