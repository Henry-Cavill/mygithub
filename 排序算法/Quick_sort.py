def partition(m_list, left, right):
    tmp = m_list[left]
    while left < right:
        # 循环初始条件就是右边大于标签值
        while left < right and m_list[right] >= tmp:
            right -= 1
        m_list[left] = m_list[right]
        while left < right and m_list[left] <= tmp:
            left += 1
        m_list[right] = m_list[left]
    # 把该值放到中间
    m_list[left] = tmp
    return left


def quick_sort(m_list, left, right):
    # 如果两个数不重合，则表明两个数还需要进行比较排序
    if left < right:
        mid = partition(m_list, left, right)
        quick_sort(m_list, left, mid - 1)
        quick_sort(m_list, mid + 1, right)


if __name__ == '__main__':
    li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
    quick_sort(li, 0, 8)
    print(li)