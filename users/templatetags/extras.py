from django import template

register = template.Library()


@register.filter(name='strip_out')
def strip_out(value, arg):
    """
    This cuts out all values of "arg" from the given string
    """
    return value.replace(arg, '')
