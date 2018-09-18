# 文件读写
with open('../lxf.txt', 'w', encoding='utf-8') as f:
    f.write('Hello,world!')


with open('../lxf.txt', 'r') as f:
    print(f.read())
# StringIO和BytesIO
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())
# 操作文件和目录
import os 
os.name
# os.environ
os.path.abspath('.')
os.path.join('E:\\','testdir')
os.mkdir('E:\\testdir')
os.rmdir('E:\\testdir')
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# 序列化
import pickle
d = dict(name='Bob', age=20, score=96)
pickle.dumps(d)
import json
obj = dict(name='小明', age=20)
s= json.dumps(obj, ensure_ascii=True)
print(s)