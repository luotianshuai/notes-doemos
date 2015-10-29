#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#I have Readme ,if you have any question you can check it !
#
import getpass
import os

print """ ��ӭ��¼����¼���̿���̨
����1�������û�
����2������û�
����3��ɾ���û�
"""

function_name = raw_input("�����빦�ܣ�1-3����")
if function_name == "1":
    print '''Ŀǰ�����˻�Ϊ��'''
    print "-------------------------------------------"
    f = file('lockuser','r')
    list_f = f.readlines()
    for line_list in list_f:   #��ӡ�����б�start
        line_list = line_list.strip()
        print line_list        #��ӡ�����б�end
    f.close
    print "-------------------------------------------"


    
    for i in range(3):
        name_1 = raw_input("�������û�����")
        f = file('lockuser','r')   #
        new_f = file('new_lockuser','a') 
        list_file = f.readlines()
        for line in list_file:
            if name_1 in line:
                line = line.replace(line,'\n')  #�滻������û�Ϊ�հ��У�
                
                print "�û�%s�ѽ����������µ�¼��" % name_1
                continue   #ִ�гɹ�����������ѭ���������������ݲ�����
            new_f.write(line)    #д���ļ�
            
        f.close()
        new_f.close()
        os.rename('new_lockuser','lockuser')  #�滻���ļ�
        break
    else:
        print "�û���Ч����������"

elif function_name == "2":
    print '''Ŀǰ�����û�Ϊ��
��ע���û���������'''
    print "-------------------------------------------"
    f = file('userlist','r')   #
    new_f = file('new_userlist','a') 
    list_file = f.readlines() #�������
    for line_list in list_file:   
        line_list = line_list.strip()
        print line_list        #��ӡ�û��б�
    print "--------------------------------------------"
    add_username = raw_input("����������Ҫ��ӵ��û�����")
    add_pwd = raw_input("������Ҫ����û������룺") 
    name_none = []
    name_none.append(add_username)
    name_none.append(add_pwd)
    name_list = ";".join(name_none)
    print name_list
    if add_username.strip != '' and add_pwd != '':
        open_userlist = file('userlist','a')
        open_userlist.write(name_list)
        open_userlist.write(';')
        open_userlist.write('\n')
        open_userlist.close
        print "�û�%s�����"  % add_username             
elif function_name == "3":
    print '''Ŀǰ��Ч�û�Ϊ��'''
    print "-------------------------------------------"
    f = file('userlist','r')   #
    new_f = file('new_userlist','a') 
    list_file = f.readlines() #�������
    for line_list in list_file:   
        line_list = line_list.strip()
        print line_list        #��ӡ�û��б�
    f.close
    print "-------------------------------------------"
    for i in range(3):
        name_userlist = raw_input("������Ҫɾ�����û�����")
        f = file('userlist','r')   #
        new_f = file('new_userlist','w') 
        list_file = f.readlines()
        for line in list_file:
            if name_userlist in line:
                line = line.replace(line,'\n')  #�滻������û�Ϊ�հ��У�
                
                print "�û�%s��ɾ����" % name_userlist
                continue   #ִ�гɹ�����������ѭ���������������ݲ�����
            new_f.write(line)    #д���ļ�
            
        f.close()
        new_f.close()
        os.rename('new_userlist','userlist')  #�滻���ļ�
        break
    else:
        print "�û���Ч����������"
else:
    print "��Ч�Ĺ�����������1-3��"