# 数字
a = "111"
print(type(a))

b = int(a)
print(type(b))

c = "0011"
print(int(c))
print(int(c, base=2))

d = 8
print(d.bit_length())

e = 1.23
print(type(e))

# 字符串
str = "Hello"
print(str.lower())
print(str.center(11, "-"))

# 循环
for i in range(5):
    print("i=", i)
