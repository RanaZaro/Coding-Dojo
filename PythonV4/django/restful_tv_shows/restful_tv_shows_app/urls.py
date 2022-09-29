from django.urls import path
from . import views

urlpatterns = [
    path('',views.index2 ),
    path('shows',views.index),
    path('shows/new',views.new),
    path('shows/<int:show_id>/edit',views.edit),
    path('shows/<int:show_id>',views.show),
    path('create',views.create),
    path('update/<int:show_id>',views.update),
    path('delete/<int:show_id',views.delete),


]
