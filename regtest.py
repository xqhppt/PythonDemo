import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello', re.S)

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello python')

if match:
    print(match.group())

