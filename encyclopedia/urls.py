from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name = 'entry'),
    path("search", views.search , name = "search "),
    path("newpage/" , views.gotoPage, name = "newpage"),
    path("save", views.savepage, name = "save"),
    path("edit", views.editpage, name = "edit"),
    path("saveedit", views.saveedit, name = "edit"),
    path("randompage", views.randompage, name = 'random'),
]
