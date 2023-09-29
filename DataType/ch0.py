import keyword

# print("hello, world")

'''
print(keyword.kwlist)
print(len(keyword.kwlist))
'''

# a, b, c, d = 20, 5.5, True, 4+3j
# print(type(a), type(b), type(c), type(d))
# print(isinstance(a, int))
#
# # 复合数据类型：列表
# li = ["iceymoss", "18", "深圳", "golang后端开发"]
# uli = ["本科", "gis", "cs"]
# for i in range(len(li)):
#     print(li[i])
# for i in li:
#     print(i)
# info = li+uli
# info.append("python")
# info.append("无锡")
# print(info)
# print(info.pop())
# print(info)
#
# # 集合
# user1_stra = {"英雄联盟解说", "罗翔说刑法", "宋浩老师"}
# user2_stra = {"偶像练习生蔡徐坤","ikun","宋浩老师","影视飓风","汤姆老师"}
# # 差集：对方还关注了
# print(user2_stra-user1_stra)
# # 并集
# print(user1_stra | user2_stra)
# # 交集：共同关注
# print(user2_stra & user1_stra)
# # 补集
# print(user2_stra ^ user1_stra)

# 字典
# map = dict()
# map["name"] = "iceymoss"
# map["age"] = 18
# map["gender"] = "1"
# for k in map:
#     print(map[k])
# print(map.keys(), map.values())

x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"
print(z)

if __name__ == "__main__":
  print()