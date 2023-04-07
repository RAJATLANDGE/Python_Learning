

# try:
#     try:
#         pass
#     except:
#         pass
# except:
#     try:
#         pass
#     except:
#         pass
#     else:
#         pass
# else:
#     try:
#         pass
#     except:
#         pass
#     finally:
#         pass
# finally:
#     try:
#         pass
#     except:
#         pass
#     else:
#         pass
#     finally:
#         pass



def fun1():
    yield 1
    yield 2

data = [1]
d = {"status": "Done"}
x = input("inter comma separated numbers")
x = x.split(",")

import json


try:
    print(1)
    print(data)
    print(data[-1])
    print(d["status"])
    fu = fun1()
    print(next(fu))
    print(3)
    print(next(fu))
    print(next(fu))
    f = open("yyyy.txt")
    print(4)
    print(10+"20")
    print(5)
    s = '{"key1": "value1", "key2": "value2", "data": ["1","2"]}'
    print(6)
    data = json.loads(s)
    print(7)
    data = data["data"][3]
    print(8)
except IndexError:
    print(9)
except ValueError:
    print(10)
except StopIteration:
    print(11)
except(KeyError, TypeError):
    print(12)
except FileNotFoundError:
    print(13)
except Exception:
    print(14)
else:
    print(15)
finally:
    print(16)

