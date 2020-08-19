from django.urls import path

from . import views

# This will be listen to /webhooks/example
urlpatterns = [
    path('example/', views.example)
]
