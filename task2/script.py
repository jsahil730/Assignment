from matplotlib import image
import numpy as np
import pandas as pd
import itertools

eqns = open('/home/sahil/CTF-practice/Assignment/task2/output.txt','r')

def load_syms():
    sym_f = open('/home/sahil/CTF-practice/Assignment/task2/vals.txt','r')
    syms_l = []
    while True:
        op = []
        for i in range(7):
            op.append(sym_f.readline().strip())
        val = sym_f.read(1)
        l = [[(ord(c)-ord('0'))*255 for c in s] for s in op]
        m = np.array(l,dtype=np.uint8)
        syms_l.append(m)
        if (val == ''):
            break
    vals_l = ['0','1','2','3','4','5','6','7','8','9','(',')','+','-','*','//']

    return (vals_l,syms_l)

vals,syms = load_syms()       

def read_eqn(a):
    m,n = np.shape(a)
    assert(m == 7)
    i = 0
    op = []
    b = np.empty((7,0),dtype=np.uint8)
    while (i < n):
        if (np.all(a[:,i] == 0)):
            _,x = np.shape(b)
            if x != 0:
                op.append(b)
                b = np.empty((7,0),dtype=np.uint8)
        else:
            f = np.reshape(a[:,i],(7,1))
            b = np.append(b,f,axis=1)
        i += 1
    _,x = np.shape(b)
    if (x != 0):
        op.append(b)
    s = ''
    for i in range(len(op)):
        for j in range(len(syms)):
            if (np.array_equal(op[i],syms[j])):
                v = j
                break
        if (v is None):
            print("error, some issue")
        s += vals[v]
    return s

it = 1
lines = []
while True:
    op = []
    for i in range(7):
        op.append(eqns.readline().strip())
    val = eqns.read(1)
    l = [[(ord(c)-ord('0'))*255 for c in s] for s in op]
    i = np.array(l,dtype=np.uint8)
    print((read_eqn(i)))
    it += 1

    if (val == ''):
        break