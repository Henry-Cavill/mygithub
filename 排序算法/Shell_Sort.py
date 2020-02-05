def shell_sort(a_list):
    n = len(a_list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):   # 因为跳过一个步长，同前一个位置的元素进行比较
            j = i
            # 只是进行插入比较
            while j > 0 and a_list[j] < a_list[j - gap]:
                a_list[j], a_list[j - gap] = a_list[j - gap], a_list[j]
                j -= gap   # 相当于跳了一个步长同次前面的位置进行比较
        gap //= 2


if __name__ == '__main__':
    alist = [2, 3, 15, 7, 1, 9, 6, 3, 8, 11]
    shell_sort(alist)
    print(alist)