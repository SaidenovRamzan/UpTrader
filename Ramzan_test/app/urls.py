from django.urls import path
from app.views import MenuView


urlpatterns = [
    path("menu/<str:menu_url>/", MenuView.as_view(), name="menu"),
    path("menu", MenuView.as_view(), name="menu"),
]
