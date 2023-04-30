from django.urls import path
from django.views.generic import TemplateView

from .views import (CategoryDetailView, CategoryView, RecipeDetailView, RecipeView, ReviewView)

urlpatterns = [
    path("recipes/", RecipeView.as_view({"get": "list"})),
    path("categories/", CategoryView.as_view({"get": "list"})),
    path("recipes/<int:pk>/", RecipeDetailView.as_view({"get": "retrieve"})),
    path("categories/<int:pk>/", CategoryDetailView.as_view({"get": "list"})),
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",

        ),
        name="swagger-ui",
    ),
]