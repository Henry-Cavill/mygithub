def isPossibleDivide(m_List, k):
    # [1, 2, 2, 3, 3, 3, 4, 4, 5, 9, 10, 11]
    if len(m_List) % k != 0:
        return False
    nums = sorted(m_List)
    for i in range(len(nums)):
        if nums[i] > 0:
            min = nums[i]
            count = 0
            j = i
            while j < len(nums) and count < k:
                if nums[j] == min:
                    count += 1
                    min += 1
                    nums[j] = 0
                else:
                    j += 1
            if count < k:
                return False
    return True


if __name__ == '__main__':
    m_List = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
    k = 3
    print(isPossibleDivide(m_List, k))
