x = 50

def tran_global():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)

tran_global()
print('Value of x is', x)