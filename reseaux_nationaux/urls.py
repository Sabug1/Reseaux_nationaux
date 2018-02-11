from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view() ,name='home'),
    path('edit_personne', views.editPersonne ,name='edit_personne'),
]
