from django.urls import path
from app.views import MenuView


urlpatterns = [
    path("menu/<str:menu_name>/", MenuView.as_view(), name="menu"),
]
