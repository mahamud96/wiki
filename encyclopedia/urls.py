from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.page, name="page"),
    path("search/", views.search, name="search"),
    path("newarticle/", views.new_article, name="new_article"),
    path("editarticle/", views.edit_article, name="edit_article"),
    path("savechanges/", views.save_changes, name="save_changes")
]
