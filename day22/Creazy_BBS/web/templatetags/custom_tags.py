#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

def tree_search(d_dic,comment_obj):#这里不用传附近和儿子了因为他是一个对象,可以直接找到父亲和儿子
    for k,v_dic in d_dic.items():
        if k == comment_obj.parent_comment:#如果找到了
            d_dic[k][comment_obj] = {} #如果找到父亲了,你的把自己存放在父亲下面,并把自己当做key,value为一个空字典
            return
        else:#如果找不到递归查找
            tree_search(d_dic[k],comment_obj)



def generate_comment_html(sub_comment_dic,margin_left_val):
    #先创建一个html默认为空
    html = ""
    for k,v_dic in sub_comment_dic.items():#循环穿过来的字典
        html += "<div style='margin-left:%spx'  class='comment-node'>" % margin_left_val + k.comment + "</div>"
        #上面的只是把第一层加了他可能还有儿子,所以通过递归继续加
        if v_dic:
            html += generate_comment_html(v_dic,margin_left_val+15)
    return html



@register.simple_tag
def build_comment_tree(comment_list):

    '''
    把评论传过来只是一个列表格式(如下),要把列别转换为字典,在把字典拼接为html
    [<Comment: <A,user:罗天帅>>, <Comment: <A2-1,user:罗天帅>>, <Comment: <A3-1,user:罗天帅>>, <Comment: <A2-2,user:罗天帅>>,
    <Comment: <A4-1,user:罗天帅>>, <Comment: <A4-2,user:罗天帅>>, <Comment: <A5-1,user:罗天帅>>, <Comment: <A3-2,user:罗天帅>>,
     <Comment: <B2,user:罗天帅>>, <Comment: <B2-1,user:罗天帅>>]
    :param comment_list:
    :return:
    '''
    comment_dic = {}
    #print(comment_list)
    for comment_obj in comment_list: #每一个元素都是一个对象
        if comment_obj.parent_comment is None: #如果没有父亲
            comment_dic[comment_obj] = {}
        else:
            #通过递归找
            tree_search(comment_dic,comment_obj)

    # #测试:
    for k,v in comment_dic.items():
        print(k,v)

    # 上面完成之后开始递归拼接字符串

    #div框架
    html = "<div class='comment-box'>"
    margin_left = 0
    for k,v in comment_dic.items():
        #第一层的html
        html += "<div class='comment-node'>" + k.comment + "</div>"
        #通过递归把他儿子加上
        html += generate_comment_html(v,margin_left+15)
    html += "</div>"
    return mark_safe(html)