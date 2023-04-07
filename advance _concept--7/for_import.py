def test():
    print("for import")
    print("second line of import")

# test()

from functools import wraps
import time

def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f"function execution took {t2 - t1} second")
        return result
    return inner



if __name__ == '__main__':                           #type main then this function--3 is show
    test()



