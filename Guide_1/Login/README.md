### 博客地址
[Python之路【第三篇】：Python基础（二）](http://www.cnblogs.com/luotianshuai/p/4949497.html)


### 程序功能

这个程序是一个登陆程序,3次登陆后锁定输入3次错误的用户:


1、运行程序:python login.py


2、程序测试:

> * login success：
```python
您好请输入您的用户名：tianshuai
您好请输入您的密码：123
欢迎tianshuai登录系统
```

> * login failure：
```python
您好请输入您的用户名：tianshuai
您好请输入您的密码：test
tianshuai的密码错误
您好请输入您的用户名：tianshuai
您好请输入您的密码：test
tianshuai的密码错误
您好请输入您的用户名：tianshuai
您好请输入您的密码：test
tianshuai的密码错误
您好请输入您的用户名：tianshuai
您好请输入您的密码：lskdjf
tianshuai用户账户已被锁定请联系管理员解锁
```