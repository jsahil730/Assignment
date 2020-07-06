from matplotlib import image
import numpy as np

f = open('/home/sahil/CTF-practice/Assignment/task2/output.txt','r')

it = 1
while True:
    op = []
    for i in range(7):
        op.append(f.readline().strip())
    val = f.read(1)
    if (val == ''):
        break
    l = [[(ord(c)-ord('0'))*255 for c in s] for s in op]
    i = np.array(l)
    image.imsave('img{}.png'.format(str(it).zfill(3)),i)
    it += 1