def println(str):
    print(f'{str}\n'.format(str))


def get_max(x, y):
    if x > y:
        print('{} is max'.format(x))
    else:
        print('{} is max'.format(y))


def say(message, times=1):
    print(message * times)


def total(a=5, *numbers, **phonebook):
    print('a', a)

    # 遍历元组中的所有项
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


def get_sum(*nums):
    sum = 0
    for i in nums:
        sum += i
    print("sum:",sum)


def search_val(tag, arr):
    for i in arr:
        if tag == i:
            return True
    return False


def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # 如果有必要，将参数转为整数
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)


# println("iceymoss")
# println("hello")

print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))

get_sum(32, 43, 54, 23, 54, 19)

get_max(10, 20)

print(search_val(20, [1, 34, 54, 23, 22]))
