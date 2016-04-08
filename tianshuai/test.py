#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'

'''
def add_end(args):
    print args
print add_end('shuaige')
'''
'''
shuaige   === print args
None  == print add_end('shuaige')

因为函数没有返回值当你去print的时候为空所以这个时候获取结果的时候直接调用函数即可
add_end('shuaige') #这样就能获取到结果
'''
'''
def add_end(args):
    a = 1
    b = 2
add_end('shuaige')

'''
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from  multiprocessing import Process,Pool
import time

def Foo(i):
    time.sleep(2)
    return i+100

def Bar(arg):
    print arg

pool = Pool(5) #创建一个进程池
pool.apply(Foo,(1,)) #去进程池里去申请一个进程去执行Foo方法

#apply 主动的去执行
#pool.apply_async(func=Foo, args=(i,),callback=Bar) 相当于异步，当申请一个线程之后，执行FOO方法就不管了，执行完之后就在执行callback ，当你执行完之后，在执行一个方法告诉我执行完了
#callback 有个函数，这个函数就是操作的Foo函数的返回值！


print 'end'
pool.close()
pool.join()#进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。

'''

def fun1():
    global var
    var = ' Baby '
    return fun2(var)

def fun2(var):
    var += 'I love you'
    fun3(var)
    return var

def fun3(var):
    var = ' 小甲鱼 '

print(fun1())