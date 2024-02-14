from django.views.generic import TemplateView
from app.models import MenuItem


class MenuView(TemplateView):
    template_name = "menu_template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_name = kwargs["menu_name"]
        menu_items = MenuItem.objects.filter(
            parent__isnull=True, title=menu_name
        ).prefetch_related("children")

        context["menu_items"] = menu_items
        return context
