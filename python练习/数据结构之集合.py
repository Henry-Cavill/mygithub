# python中的集合不允许有重复的元素

set1 = {1, 2, 3, 3, 3, 2}
set2 = set(range(1, 10))
set2.update([11, 12])
# # 1.求长度
# print(len(set1))
#
# # 2.增加元素
# set1.add(4)
#
# print(set2)
# 1.集合求交集
print(set1 & set2)

# 2.集合求并集
print(set1 | set2)

# 3.集合求差集
print(set1 - set2)