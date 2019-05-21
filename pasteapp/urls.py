from django.urls import path
from .views import index, retrieve_objects

urlpatterns = [
        path('', index),
        path('paste/<str:paste_url>/', retrieve_objects)
        ]

