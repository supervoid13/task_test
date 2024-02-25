from django import template

from menu.models import Item


class Level:

    def __init__(self, level: int):
        self.level = level

    def increment(self):
        self.level += 1
        return ''


register = template.Library()


@register.inclusion_tag("list_menus.html")
def draw_menu(menu_name: str, max_level: int, tree: list[str]) -> dict[str, int]:
    items = Item.objects.filter(parent__isnull=True, title=menu_name).prefetch_related("item_set")
    return {
        "items": items,
        "level": Level(0),
        "max_level": max_level,
        "tree": tree,
    }
