def repeatedSubstringPattern(s):
    """
        1.先确定重复字符串的长度
        2.然后依次进行比较该步长的元素是否为重复的字符
    """
    length = len(s)
    for i in range(1, length//2+1):
        if length % i == 0 and s[:i]*(length // i) == s:
            return True
    return False


if __name__ == '__main__':
    s = 'abcabcabcabc'
    print(s[1:-1])
    print(s[0:-1])
    # print(repeatedSubstringPattern(s))