# 讲道理看的不是很懂
def hanno(n, a, b, c):   # a移动到c位
    if n > 0:
        hanno(n-1, a, c, b)   # 从a经过c移动到b
        print('%s -> %s' % (a, c))
        hanno(n-1, b, a, c)   # 从b经过a移动到c


if __name__ == '__main__':
    hanno(2, 'a', 'b', 'c')
    pass
