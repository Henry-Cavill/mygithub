def insert_sort(alist):
    """从后向前比较，如果当前元素小于前一个，则进行交换"""
    for i in range(1, len(alist)):
        tmp = alist[i]
        j = i-1
        while j >= 0 and alist[j] > tmp:
            alist[j+1] = alist[j]
            j -= 1
        alist[j+1] = tmp


if __name__ == '__main__':
    m_list = [2, 3, 15, 7, 1, 9, 6, 3, 8, 11]
    insert_sort(m_list)
    print(m_list)
