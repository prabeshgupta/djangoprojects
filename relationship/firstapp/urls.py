from django.urls import path
from . import views

urlpatterns = [
    path('relationship/', views.relationship, name='relationship')
]