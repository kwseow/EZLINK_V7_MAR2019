a = "python or java"
b = a.split(" ")
print(b)
# ['python', 'or', 'java']

b = a.split("on")
print(b)
# ['pyth', ' or java']

a_list = ['python', 'or', 'java']
seperator = " "
b = seperator.join(a_list)
print(b)
# "python or java"

seperator = ","
c = seperator.join(a_list)
print(c)
# "python,or,java"