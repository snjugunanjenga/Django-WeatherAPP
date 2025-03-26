from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('favorites/', views.favorites, name='favorites'),
    path('add_favorite/', views.add_favorite, name='add_favorite'),
    path('remove_favorite/<int:location_id>/', views.remove_favorite, name='remove_favorite'),
    path('set_default_location/', views.set_default_location, name='set_default_location')
]

