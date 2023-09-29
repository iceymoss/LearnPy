# print 打印一个hello
# print("hello, iceymoss!")

age = 18
name = "iceymoss"

# 直接填写在占位符
print(f'age:{age}, name:{name}'.format())

# 指定类型
print('age:{0}, name:{1}'.format(age, name))

age = 20
name = 'Swaroop'

print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

a = 3
b = 4
print('a: {0:.3f}, b: {1:.4f}'.format(a, b))

# 取十进制小数点后的精度为 3 ，得到的浮点数为 '0.333'
print('{0:.3f}'.format(1.0/3))
# 填充下划线 (_) ，文本居中
# 将 '___hello___' 的宽度扩充为 11
print('{0:_^11}'.format('hello'))
# 用基于关键字的方法打印显示 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# 间隔符
print("hello", end=" ")
print('hello')

# 转义符
print("What\'s your name?")

# 换行符
print("hello\niceymoss!")

