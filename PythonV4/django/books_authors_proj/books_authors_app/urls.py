from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addbook', views.addbook),
    path('books/<int:id>', views.viewbook),
    path('authtobook/<int:id>', views.authtobook),
]
