from django import template

register = template.Library()


def strip_out(value, arg):
    """
    This cuts out all values of "arg" from the given string
    """
    return value.replace(arg, '')


register.filter('strip_out', strip_out)
