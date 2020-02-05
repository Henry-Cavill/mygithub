def printReserve(s):
    def reservr(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            reservr(left + 1, right - 1)
    # reservr(0, len(s) - 1)

    def reservr(left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    reservr(0, len(s) - 1)


s = ["h", "e", "l", "l", "o"]
printReserve(s)
print(s)
