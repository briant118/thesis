from django import template
import re

register = template.Library()

@register.filter
def get_int(value):
    try:
        value = re.search(r'\d+', str(value)).group()
        return int(value)
    except (ValueError, TypeError):
        return None