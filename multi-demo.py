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
    return int(a) + b

def main():

    args = [1,5,7]
    arg = 1
    partial_func = partial(func,b=arg)
    pool = Pool(2)
    results = []

    for i in args:
        y = pool.apply_async(partial_func,str(i))
        results.append(y)

    pool.close()
    pool.join()
    results = [res.get() for res in results]
    print(results)

if __name__=="__main__":
    dir = "C:/Users/Administrator/Desktop/LIDC-IDRI-0865/01-01-2000-CT THORAX WCONTRAST-81073/3-10561"
    fnms = list_files(dir)
    fnms.sort()
    main()
