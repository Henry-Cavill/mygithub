def repeatedSubstringPattern(s):
    """
        1.先确定重复字符串的长度
        2.然后依次进行比较该步长的元素是否为重复的字符
    """
    length = len(s)
    if length <= 0:
        return False
    index = 0
    count = 1  # 表示子串的长度
    for i in range(1, len(s)):
        if s[i] != s[index]:
            count += 1
            continue
        if s[i] == s[index]:
            for n in range(count, len(s)):
                j = n
                if s[index] == s[n]:
                    continue
                else:
                    return False
    return True


if __name__ == '__main__':
    s = 'abcabcabcabc'
    print(repeatedSubstringPattern(s))