import json

data = {"name": "hello", "age": 18, "remark": "this is remark"}

dataString = json.dumps(data)
print(dataString)

# 格式化输出
dataString = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
print(dataString)

dataObj = json.loads(dataString)
print(dataObj)