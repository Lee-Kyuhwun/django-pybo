from django import template

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

# 템플릿 필터 함수
