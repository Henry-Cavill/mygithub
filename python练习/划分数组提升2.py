import collections


def isPossibleDivide(nums, k):
    nums.sort()
    dic = collections.defaultdict(int)
    for num in nums:
        dic[num] += 1
    for num in nums:
        while dic[num] != 0:
            for i in range(k):
                if dic[num + i] == 0:
                    return False
                dic[num + i] -= 1
    return True


if __name__ == '__main__':
    m_List = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
    k = 3
    print(isPossibleDivide(m_List, k))