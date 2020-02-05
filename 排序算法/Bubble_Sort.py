def bubble_sort(list):
    for j in range(len(list)):
        for i in range(0, len(list)-1-j):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    print(list)


if __name__ == '__main__':
    m_list = [2, 3, 15, 7, 1, 9, 6, 3, 8, 11]
    bubble_sort(m_list)
