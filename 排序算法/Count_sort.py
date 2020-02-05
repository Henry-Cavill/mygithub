def count_sort(li, max_len):
    # 设置一个含有最大长度的全0列表
    count = [0 for _ in range(max_len + 1)]
    # 遍历该列表，把出现元素对应在count列表该元素对应位置的下标加一
    for i in li:
        count[i] += 1
    li.clear()
    # i位置的元素出现v次
    for i, v in enumerate(count):
        for _ in range(v):
            li.append(i)
    return li


if __name__ == '__main__':
    li = [4, 5, 5, 20, 5, 2, 1, 0, 4, 5, 8, 7, 3]
    sort_li = count_sort(li, 20)
    print(sort_li)
