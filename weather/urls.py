from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('favorites/', views.favorites, name='favorites'),
    path('add_favorite/', views.add_favorite, name='add_favorite'),
    path('remove_favorite/<int:location_id>/', views.remove_favorite, name='remove_favorite'),
    path('set_default_location/', views.set_default_location, name='set_default_location'),
    path('demo-login/', views.demo_login, name='demo_login'),
    path('farmer_dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('pilot_dashboard/', views.pilot_dashboard, name='pilot_dashboard'),
]

