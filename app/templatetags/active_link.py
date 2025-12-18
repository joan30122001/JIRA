from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, url_name):
    request = context.get('request')
    if request and hasattr(request, "resolver_match"):
        if request.resolver_match and request.resolver_match.url_name == url_name:
            return "active"
    return ""
