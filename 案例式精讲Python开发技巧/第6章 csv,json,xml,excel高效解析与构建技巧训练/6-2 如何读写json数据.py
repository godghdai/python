# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 6-2 如何读写json数据
import json

"""
import requests
import json
# 录音
from record import Record

record = Record(channels=1)
audioData = record.record(2)

# 获取token
from secret import API_KEY, SECRET_KEY

authUrl = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" \
          + API_KEY + "&client_secret=" + SECRET_KEY;
response = requests.get(authUrl)
res = json.loads(response.content)
token = res['access_token']

# 语单识别
cuid = 'xxxxxxx'
srvUrl = 'http://vop.baidu.com/server_api' + '?cuid' + cuid + "&token" + token
httpHeader = {
    'Content-Type': 'audio/wav;rate=8000',
}
response = requests.post(srvUrl, headers=httpHeader, data=audioData)
res = json.loads(response.content)
text = res['result'][0]

print u'\识别结果：'
print text;

"""

l = [1, 2, 'abc', {'name': 'Bob', 'age': 13}]
print json.dumps(l)
d = {'b': None, 'a': 5, 'c': 'abc'}
print json.dumps(d)
# 去除多余空格
print json.dumps(l, separators=[',', ':'])
"""
[1, 2, "abc", {"age": 13, "name": "Bob"}]
[1,2,"abc",{"age":13,"name":"Bob"}]
"""

print json.dumps(d, sort_keys=True)
# {"a": 5, "b": null, "c": "abc"}


l2 = json.loads('[1, 2, "abc", {"age": 13, "name": "Bob"}]')
print l2[0]

d2 = json.loads('{"a": 5,"b": null,"c": "abc"}')
print d2['a']

# 写入文件
with open('./files/demo.json', 'wb') as f:
    json.dump(l, f)
