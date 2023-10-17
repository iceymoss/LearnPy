def use_logging(func):
    def wrapper(*args, **kwargs):
        print("[debug] bar is running" % func.name)
        return func(*args, **kwargs)

    return wrapper


def bar():
    print("I am bar")


use_logging()
