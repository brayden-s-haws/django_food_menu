from django import template

register = template.Library()

@register.filter(name='currency')
def currency(value):
    return f"${value}"

@register.filter(name='discount')
def discount(value,percentage):
    return int(value) - (int(value) *  (int(percentage)/100))