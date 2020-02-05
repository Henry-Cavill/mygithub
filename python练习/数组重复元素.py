def findDuplicates(nums):
    m_list = []
    for i in nums:
        # 首先将数组依次遍历，判断该数字对应数组下标的位置是否为整数
        # 如果是正数，则表明该数字为第一次出现，如果为负数，则表示该数字已经重复出现过了
        if nums[abs(i)-1] > 0:
            nums[abs(i)-1] *= -1
        else:
            m_list.append(abs(i))

    print(m_list)


if __name__ == '__main__':
    list = [4, 3, 2, 7, 8, 2, 3, 1]
    findDuplicates(list)