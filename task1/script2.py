import itertools,random

sentence = 'Some multiple of 3 byte words with no repetition'
l = [sentence[3*i:3*(i+1)] for i in range(len(sentence)//3)]
f = open('output.txt','wb')
chrs = list(itertools.product([chr(i) for i in range(256)],repeat=3))
random.shuffle(chrs)
for i in chrs:
    x = ''.join(i)
    if (x not in l):
        f.write(x.encode('latin1'))
        f.write(b'\n')