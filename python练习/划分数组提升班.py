from collections import Counter


def isPossibleDivide(nums, k):
    # 统计元素出现的个数
    s = Counter(nums)
    ordered_nums = sorted(s)
    for num in ordered_nums:
        occ = s[num]
        if s[num] > 0:
            for i in range(num + 1, num + k):
                if s[i] >= occ:
                    s[i] -= occ
                else:
                    return False
    return True


if __name__ == '__main__':
    nums = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
    k = 3
    isPossibleDivide(nums, k)
