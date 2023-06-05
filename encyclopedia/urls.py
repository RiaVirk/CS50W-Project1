from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("new/", views.new_page, name="new_page" ),
    path("edit/", views.edit, name="edit" ),
    path("edit_saved/", views.edit_saved, name="edit_saved" ),
    path("rndm/", views.rndm, name="rndm" ),
]
