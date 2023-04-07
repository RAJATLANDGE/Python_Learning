import sys

x = sys.argv

print(x)

input = ("inter a number")

numbers = [int(d) for d in x[1:]]

print(sum(numbers))

data1 = [90, 55, 63]
print(sys.getsizeof(data1))


sys.exit(0)      # execution is off from that line