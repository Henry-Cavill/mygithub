def maxProfit(prices):
    count = 0
    for i in range(1, len(prices)):
        tmp = prices[i] - prices[i-1]
        if tmp > 0:
            count += tmp
    return count


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    p = maxProfit(prices)
    print(p)