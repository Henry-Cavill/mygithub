def selection_sort(alist):
    """每次对比将队列中的最小元素置换到第一个"""
    for i in range(len(alist)):
        mid_index = i
        for j in range(i, len(alist)):
            if alist[j] < alist[mid_index]:
                mid_index = j
        if mid_index != i:
            alist[i], alist[mid_index] = alist[mid_index], alist[i]


if __name__ == '__main__':
    m_list = [2, 3, 15, 7, 1, 9, 6, 3, 8, 11]
    selection_sort(m_list)
    print(m_list)