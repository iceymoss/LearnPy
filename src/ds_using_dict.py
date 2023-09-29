user = {
    "id": 1,
    "name": "iceymoss",
    "age": 23
}

print(user)

# 添加key
user["from"] = "guizhou"
print(user)

# 删除key
del user["from"]

# 获取值
print(user["name"])

# 获取长度
print(len(user))

if 'name' in user:
    print(user['name'])

# 遍历
for k, v in user.items():
    print('key:{0}, value:{1}'.format(k, v))



