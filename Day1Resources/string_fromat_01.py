import math
a = math.pi
print(a)
# 3.141592653589793

b = 5
c = "python"
line = "%s %f %d" % (c, a, b)
print(line)
# python 3.141593 5

line = "%03d" % (b)
print(line)
# 005