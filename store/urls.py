from django.contrib import admin
from django.urls import path
from .views import view_books
from .views import view_books, view_cached_books,post_books


urlpatterns = [
    path('',view_books),
    path('cache/', view_cached_books),
    path('book/',post_books),


]




