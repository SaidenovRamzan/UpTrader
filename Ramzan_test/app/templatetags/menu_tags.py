from django import template
from app.models import MenuItem


register = template.Library()


@register.simple_tag()
def draw_menu(menu_url: str = None):
    menu_html = ""

    if not menu_url:  # Если нет url, то передаем все корневые папки
        menu_items = MenuItem.objects.filter(parent__isnull=True).prefetch_related(
            "children"
        )
        menu_html = "<ul>"
        for item in menu_items:  # Пишем всех родителей
            menu_html += f'<li><a href="http://localhost:8000/menu/{ item.url }">{item.title}</a>'
            for child in item.children.all():  # Пишем всех детей
                menu_html += f"""
                    <ul>
                        <li>
                            <a href="http://localhost:8000/menu/{ child.url }">{child.title}</a>
                        </li>
                    </ul>
                """
            menu_html += "</li>"
        menu_html += "</ul>"

        return menu_html

    else:
        menu_items = MenuItem.objects.prefetch_related("children", "parent").get(
            url=menu_url
        )

        for item in menu_items.children.all():  # Пишем всех детей
            menu_html += f"""
                <ul>
                    <li>
                        <a href="http://localhost:8000/menu/{ item.url }">{item.title}</a>
                    </li>
                </ul>
            """

        def get_parents(item):  # Пишем всех родителей
            nonlocal menu_html
            menu_html = f"""
                <ul>    
                    <li>
                        <a href="http://localhost:8000/menu/{ item.url }">{item.title}</a>    
                    </li>
                    {menu_html}
                </ul>
            """
            if item.parent:
                get_parents(item.parent)

        get_parents(menu_items)

        return menu_html
