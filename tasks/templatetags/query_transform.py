from django import template
from django.http import HttpRequest

register = template.Library()


@register.simple_tag
def query_transform(request: HttpRequest, **kwargs) -> str:
    """
    Returns an updated query string based on the provided keyword arguments.

    Parameters:
    - request: HttpRequest object containing the original GET parameters.
    - kwargs: key-value pairs to update or remove from the query string.

    If a value is None, the key will be removed from the query string.
    Otherwise, the key will be updated or added.

    Returns:
    - A URL-encoded query string.
    """
    updated_query = request.GET.copy()
    for key, value in kwargs.items():
        if value is not None:
            updated_query[key] = value
        else:
            updated_query.pop(key, None)
    return updated_query.urlencode()