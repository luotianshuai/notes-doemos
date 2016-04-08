#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django import template
from django.utils.safestring import mark_safe
from django.template.base import resolve_variable, Node, TemplateSyntaxError

register = template.Library()

from django import template
from django.utils.safestring import mark_safe
from django.template.base import resolve_variable, Node, TemplateSyntaxError

register = template.Library()

@register.simple_tag
def error_message(arg):
    if arg:
        return arg[0][0]
    else:
        return ''


