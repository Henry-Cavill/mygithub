def merge(m_list, low, mid, high):
    # 列表两段有序，[low, mid] [mid+1, high]
    i = low
    j = mid + 1
    li_tmp = []
    # 用来依次根据大小进行插入，如果其中某一段的值先完结
    while i <= mid and j <= high:
        if m_list[i] <= m_list[j]:
            li_tmp.append(m_list[i])
            i += 1
        else:
            li_tmp.append(m_list[j])
            j += 1
    while i <= mid:
        li_tmp.append(m_list[i])
        i += 1
    while j <= high:
        li_tmp.append(m_list[j])
        j += 1
    for i in range(low, high+1):
        m_list[i] = li_tmp[i - low]


def merge_sort(m_list, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(m_list, low, mid)
        merge_sort(m_list, mid + 1, high)
        merge(m_list, low, mid, high)


if __name__ == '__main__':
    li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
    merge_sort(li, 0, 8)
    print(li)