from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search_bar", views.search_bar, name="search_bar"),
    path("add", views.create_entry, name="add"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("create", views.display_new_entry, name="create"),
    path("random_page", views.random_page, name="random_page"),
    path("<str:title>", views.entry_page, name="entry_page")
]
