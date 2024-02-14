from django import template
from app.models import MenuItem


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context["request"]
    menu_items = MenuItem.objects.filter(
        parent__isnull=True, title=menu_name
    ).prefetch_related("children")

    def render_menu_items(items):
        menu_html = "<ul>"
        for item in items:
            active = ""
            if request.path == item.url:
                active = "active"
            menu_html += f'<li class="{active}"><a href="{item.url}">{item.title}</a>'
            if item.children.exists():
                menu_html += render_menu_items(item.children.all())
            menu_html += "</li>"
        menu_html += "</ul>"
        return menu_html

    return render_menu_items(menu_items)
