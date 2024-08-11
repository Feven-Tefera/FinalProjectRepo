from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplies the value by the arg."""
    try:
        return value * arg
    except (TypeError, ValueError):
        return ''
@register.filter
def sum(value):
    """Returns the sum of a list."""
    if isinstance(value, (list, tuple)):
        return sum(value)
    return 0