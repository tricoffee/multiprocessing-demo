# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 23:44
# @Author  : Nicholas (Liheng He)
# @FileName: multi-demo.py
# @Description Please explain the function of this file
# @ProjectName: MyCustomProject
# @Version :  1.0
import os
def list_files(dir):
    fnms = [os.path.join(dir, f).replace("\\","/") for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    return fnms
import itertools

from functools import partial
from multiprocessing import Pool

def func(a, b):
    print(a)

    idx,name = int(a[0]),a[1]

    return idx,name,b

def main(fnms):

    arg = 1
    partial_func = partial(func,b=arg)
    pool = Pool(2)
    results = []

    for i in range(len(fnms)):
        y = pool.apply_async(partial_func,zip([str(i)],[fnms[i]]))
        results.append(y)

    pool.close()
    pool.join()
    results = [res.get() for res in results]
    for res in results:
        print(res[0],res[1])

if __name__=="__main__":
    dir = "C:/Users/Administrator/Desktop/LIDC-IDRI-0865/01-01-2000-CT THORAX WCONTRAST-81073/3-10561"
    fnms = list_files(dir)
    fnms.sort()
    print(fnms)
    print("x"*18)
    #for i in range(len(fnms)):
    #    x = zip([i],[fnms[i]])
     #   idx,name= zip(*x)
     #   print(idx[0],name[0])

    main(fnms)
