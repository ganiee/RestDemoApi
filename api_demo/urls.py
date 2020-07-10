from django.contrib import admin
from django.urls import path

from api_demo.views import article_list, article_detail

urlpatterns = [
    path('article/',article_list),
    path('article/<int:pk>',article_detail)
]
