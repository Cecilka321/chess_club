from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),path('academy/', views.academy, name="academy"),
    path('attribution/', views.attribution, name="attribution"),
    path('contacts/', views.contacts, name="contacts"),
    path('gallery/', views.gallery, name="gallery"),
    path('history/', views.history, name="history"),
    path('members/', views.members, name="members"),
    path('news/', views.news, name="news"),
    path('tournaments/', views.tournaments, name="tournaments"),
    path('detail/<int:pk>/', views.detail, name="detail"),
]