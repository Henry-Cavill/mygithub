def bin_search(val, list):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low+high) // 2
        if list[mid] == val:
            return mid
        elif list[mid] < val:
            low = mid
        else:
            high = mid
    return -1


if __name__ == '__main__':
    m_list = [1, 2, 3, 5, 9, 50, 100, 120, 350]
    m = bin_search(5, m_list)
    print(m)