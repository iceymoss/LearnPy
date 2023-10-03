# 判断对称
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

data = str(input("请输入字符串："))
if is_palindrome(data):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

