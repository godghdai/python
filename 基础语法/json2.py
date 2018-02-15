'''
JSON是一种轻量级的数据交换格式。
符合JSON字符串格式的字符串叫JSON字符串
JSON 易于阅读,易于解析,网络传输效率
跨语言数据交换

json      python
object    dict
array     list
string    str
number    int 
number    float
true      True
false     False
null      None

'''
import json

# 反序列化
json_str = '{"name":"petter","age":18,"flag":false}'
student = json.loads(json_str)
# <class 'dict'>
print(type(student))
print(student)
print(student["name"])

json_str = '[{"name":"petter","age":18},{"name":"petter2","age":19}]'
student = json.loads(json_str)
# <class 'list'>
print(type(student))
print(student[0]["name"])


# 序列化
student = [
    {"name": "petter", "age": 18},
    {"name": "petter2", "age": 19}
]

json_str = json.dumps(student)
# <class 'str'>
print(type(json_str))
# [{"name": "petter", "age": 18}, {"name": "petter2", "age": 19}]
print(json_str)
