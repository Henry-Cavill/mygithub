def two_sum(li, num):
    dic = {}
    for i in range(len(li)):
        a = li[i]
        b = num - li[i]
        if b not in dic:
            dic[a] = i
        else:
            return dic[b], i


if __name__ == '__main__':
    li = [2, 8, 13, 17, 6, 12, 9, 3, 4]
    num = 26
    two_sum(li, num)