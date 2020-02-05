def max_num(nums):
    index = 0
    i = 0
    while i <= len(nums):
        if i < len(nums) and nums[i] > nums[index]:
            index = i
        i += 1
    return index


list = [3, 2, 1, 6, 0, 5, 9]
ma = max_num(list)
print(ma)
