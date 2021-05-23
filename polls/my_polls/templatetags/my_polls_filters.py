from django import template

register = template.Library()

@register.filter
def get_by_index(iterable, index):
    return iterable[index]