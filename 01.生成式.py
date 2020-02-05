# f = [i for i in range(10)]
# print(f)
#
# f2 = [x + y for x in 'ABCDE' for y in '12345']
"""
其运行结果如下所示：
list = []
for x in 'ABCDE':
    for y in '12345':
        list.append(x+y)
"""

pre = [1, 2, 4, 7, 3, 5, 6, 8]
list = pre[1:3]
print(list)