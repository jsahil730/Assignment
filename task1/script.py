import itertools
from Crypto.Util.number import *
from string import *

s = set()
for i in range(1,5):
    with open("/home/sahil/CTF-practice/Assignment/task1/part{}".format(i),"rb") as f:
        while True:
            v = f.read(3)
            s.add(bytes_to_long(v))
            op = f.read(1)
            if (op == b''):
                break
# with open("/home/sahil/CTF-practice/Assignment/task1/output.txt","rb") as f:
#     while True:
#         v = f.read(3)
#         s.add(bytes_to_long(v))
#         op = f.read(1)
#         if (op == b''):
#             break

l = [chr(i) for i in range(256)]
x = []
for i in itertools.product(l,repeat=3):
    v = ''.join(i)
    v = bytes_to_long(v.encode('latin1'))
    if (v not in s):
        x.append(''.join(i))

print(x[:20])