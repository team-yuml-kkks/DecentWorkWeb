from typing import Any

from django import template
from django.utils.safestring import mark_safe

from decentwork.apps.loader.fileloader import get_static_url

register = template.Library()


@register.simple_tag
def get_js(resource_path: str) -> Any:
    """Gets full url for javascript file with HTML tag.

    Args:
        resource_path - Path to javascript file in webserver without extension

    Returns:
        HTML tag with full url to javascript file.
    """
    url = get_static_url(resource_path, extension='js')
    return mark_safe('<script src="%s"></script>' % (url))


@register.simple_tag
def get_css(resource_path: str) -> Any:
    """Gets full url for css file with HTML tag.

    Args:
        resource_path - Path to css file in webserver without extension

    Returns:
        HTML tag with full url to css file.
    """
    url = get_static_url(resource_path, extension='css')
    return mark_safe('<link rel="stylesheet" href="%s">' % (url))


@register.simple_tag
def get_img(resource_path: str, extension: str) -> Any:
    """Gets full path to image file wih HTML tag.

    Args:
        resource_path - Path to image in webserver without extension.
        extension - Image file extension.

    Returns:
        HTML tag with full url to image file.
    """
    url = get_static_url(resource_path, extension=extension)
    return mark_safe('<img src="%s">' % (url))
