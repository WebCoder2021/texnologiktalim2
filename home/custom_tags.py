import random
from django import template
register = template.Library()

@register.filter
def shuffle(arg):
    tmp = list(arg)[:]
    random.shuffle(tmp)
    return tmp

@register.filter
def progress(num1,num2):
    
    return '{:.2f}'.format((num1*100)/num2)