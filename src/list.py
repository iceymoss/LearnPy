list = ['apply', 'huawei', 'oppo', 'xiaomi']

print(len(list))
print(list)

# 遍历
for i in range(len(list)):
    print(list[i])

for item in list:
    print(item, end=' ')

# 追加元素
list.append('rice')
print(len(list))

# 排序
list.sort()
print(list)

# 下标获取
print(list[0])

del list[0]

print(list)

