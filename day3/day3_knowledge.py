#/usr/bin/python
# --*-- coding:utf-8 --*--
"""遍历文件，当行以backend开头时，并且包含输入的域名，使flog = True 打个标记。
   当行以backend开头，或者空行开头时。停止
   打印期间的不是空行的行，就是需要查找Realserver"""

def Function_Search(search):  #查询函数

    file = open('HAproxy.cf','r')
    flog = False
    for line in file:
        if line.startswith("backend") and search in line:
                flog = True
        elif line == '\n' or line.startswith("backend"):
                break
        else:
            if flog == True and line != '\n':
                print(line.strip())
    file.close()



"""接受传来的字典。格式化字符串。
   打开一个新文件，将老配置文件循环写入新文件，判断需要删除的行，直接continue
   判断需要删除的行的方法与查询类似
"""

def Function_Delete(**delete_dict): #删除函数

    search = delete_dict['backend']
    delete_ip = delete_dict['record']
    file = open('HAproxy.cf','r')
    new_file = open('new_file','w')
    flog = False

    for line in file:
        if line.startswith("backend") and search in line:
                flog = True
        elif line.startswith("backend"):
                flog = False
        else:
            if flog == True and delete_ip in line:
                continue
        new_file.write(line)
    file.close()
    new_file.close()



"""接受传来的字典，格式化字符串
   打开一个新文件，定位到需要添加的域名，查询期间的行存不存在，如果存在就打印已存在，并删除新文件
   如果不存在，将格式化好的字符串插入
"""
def Function_Add(**add_dict):#增加函数
    import os
    search = add_dict["backend"]
    add_ip = add_dict["record"]
    file = open('HAproxy.cf','r')
    new_file = open('new_file','w')
    flog = False

    for line in file:
        if line.startswith("backend") and search in line:
                flog = True

        elif  line.startswith("backend"):
                flog = False
        else:
            if flog == True and add_ip not in line:
                new_file.write('\t\t'+add_ip+'\n')
                flog = False
			
	    elif flog == True and add_ip in line:
		print "the realserver is exist!!"
		os.remove('new_file')
		exit();
        new_file.write(line)
    file.close()
    new_file.close()

"""格式化输入，将数字和操作都放在一个字典里，供用户选择
   判断用户选择，调用不同的函数，将用户的选择格式化传给不同的函数作参数。
"""
def Function_Input(select_value):#输入函数
  import json	
  print '输入格式：查询=======> www.old.org'
  print '删除 或者 增加 ======>{"backend":"www.old.org","record":"server 100.1.7.9 100.1.7.89999 weight 20 maxconn 3000"}（老师的那破格式是字典套字典，我就不套就不套就不套）' 
  input_two = raw_input("please input>> ")
  if select_value == "check":

    Function_Search(input_two)

  elif select_value == "add_server":
     
    input_dict = json.loads(input_two)
    Function_Add(**input_dict)

  elif select_value == "delete_server":

    input_dict = json.loads(input_two)
    Function_Delete(**input_dict)

select = {1:"check",2:"add_server",3:"delete_server"}


print "----------------------------"
for value in select.keys():
  print value,select[value]
  print 


input = raw_input("请输入数字选择要执行的操作 >> ")  

Function_Input(select[int(input)])
