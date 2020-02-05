def lengthOfLongestSubstring(s):
    # 判断字符串是否为空
    if not s:
        return 0
    # 记录子串开始的标记值
    left = 0
    # 设定一个用来存放子串的集合
    lookup = set()
    n = len(s)
    max_len = 0         # 用来判断所求的最大子串长度
    cur_len = 0          # 记录遍历中的子串长度
    for i in range(n):
        cur_len += 1
        while s[i] in lookup:
            # 如果该字串在该集合中
            lookup.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len:
            max_len = cur_len
        lookup.add(s[i])
    return max_len


if __name__ == '__main__':
    S = 'abcaaabbcbb'
    max = lengthOfLongestSubstring(S)
    print(max)
