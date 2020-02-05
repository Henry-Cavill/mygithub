def longestOnes(A, k):
    i = 0
    n = len(A)
    for j in range(0, n):
        if A[j] == 0:
            k -= 1
        if k < 0:
            if A[i] == 0:
                k += 1
            i += 1
    return j - i + 1


if __name__ == '__main__':
    A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    K = 2
    print(longestOnes(A, K))
