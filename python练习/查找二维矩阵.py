def searchMatrix(matrix, target):
    found = False
    # 对应的行数
    rows = len(matrix)
    # 对应数组的列数
    columns = len(matrix[0])
    if matrix is not None and rows > 0 and columns > 0:
        # 设定一个行的下标
        row = 0
        # 设定一个列的下标
        column = columns - 1
        # 因为行数一开始为零，所以设定循环行数不大于最大行数
        # 列数循环最后不小于0
        while row < rows and column >= 0:
            if matrix[row][column] == target:
                found = True
                return found
            elif matrix[row][column] > target:
                column -= 1
            else:
                row += 1
        return found


if __name__ == '__main__':
    mli = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    found = searchMatrix(mli, 20)
    print(found)
