from django.contrib import admin
from django.urls import path
from .views import view_books


urlpatterns = [
    path('',view_books)
]




