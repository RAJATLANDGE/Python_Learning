

# num1 = int(input("Enter First Number"))
# num2 = int(input("Enter Second Number"))

# print("Division of first by second is", num1//num2)


# data = input("Enter the Number in comma separated form")

# data = data.split(",")
# data = [item.strip() for item in data]              # strip =  remove space or any pass value
# sum = 0
# for item in data:
#     sum += int(item)

# print("Total is", sum)


'''exception handling block and combination
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
    
    

try:
    pass
except:
    pass


try:
    pass
except:
    pass
else:
    pass
    
    
try:
    pass
except:
    pass
finally:
    pass
'''


# num1 = int(input("Enter First Number"))
# num2 = int(input("Enter Second Number"))
# try:
#     print("Division of first by second is", num1//num2)
# except:
#     print("cannot divide a number by zero")

# data = input("Enter the Number in comma separated form")

# data = data.split(",")
# data = [item.strip() for item in data]
# sum = 0
# for item in data:
#     try:
#         sum += int(item)
#     except:
#         sum += 0            # or give pass

# print("Total is calculated and invalid vlaue is ignore, total is ", sum)


# data = input("Enter the Number in comma separated form")
#
# data = data.split(",")
# data = [item.strip() for item in data]
# sum = 0
# try:
#     for item in data:
#         sum += int(item)
# except:
#     pass
#
# print("Total is calculated and rest data is ignored once we found some issue, total is ", sum)


# try:
#     num1 = int(input("Enter First Number"))
#     num2 = int(input("Enter Second Number"))
#     print("Division of first by second is", num1//num2)
# except:
#     print("issued occured")

# data = [11,12,13]
# try:
#     print(data[2])
#     num1 = int(input("Enter First Number"))
#     num2 = int(input("Enter Second Number"))
#     print("Division of first by second is", num1//num2)
#     print(1+"A")
# except ZeroDivisionError:
#     print("Cannot Divide By Zero")
#     #
#     #
# except ValueError:
#     print("Invalid Input")
#     #
#     #
# except IndexError:
#     print("Data Not Accessible")
#     #
#     #
# except Exception:                                        # bare exception   & always use in last
#     print("some other issue")




# try:
#     num1 = int(input("Enter First Number"))
#     num2 = int(input("Enter Second Number"))
#     print("Division of first by second is", num1//num2)
# except ZeroDivisionError as ze:
#     print(dir(ze))
#     print(ze)
#     print("cannot divide by zero")


# filename = input("Enter name of the file to open")
# try:
#     print("in try")
#     f = open(filename)
# except FileNotFoundError:
#     print("in except, filenot found error")
#     f = open(filename, "w")
#     f.write("test1")
# else:
#     print("in else")
#     print(f.read())
# finally:
#     print("in finally")
#     f.close()

import json
# data = [11,12,13]
# try:
#     s = '{"key1": "value1", "key2": "value2", "data": ["1","2"]}'
#     data= json.loads(s)
#     data = data["data"][1]
#     print(data)
#
# except ValueError:
#     print("value error")
# except KeyError:
#     print("keyerror")
# except IndexError:
#     print("index error")


# try:
#     s = '{"key1": "value1", "key2": "value2", "data": ["1","2"]}'
#     data= json.loads(s)
#     data = data["data"][3]
#
# except ValueError as e:
#     print(e.__class__)
# except KeyError as e:
#     print(e.__class__)
# except IndexError as e:
#     print(e.__class__)
#


try:
    s = '{"key1": "value1", "key2": "value2", "data": ["1","2"]}'
    data= json.loads(s)
    data = data["data"][3]
    print(data)

except (ValueError, KeyError, IndexError) as e:
    print(e.__class__)

