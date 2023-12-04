from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('consumables/', views.get_consumables),
    path('consumables/create/', views.create_consumable),
    path('consumables/<int:pk>/update/', views.update_consumable),
    path('consumables/<int:pk>/delete/', views.delete_consumable),
    path('consumables/<int:pk>/', views.get_consumable),

    path('register_user/', views.register),
    path('login_user/', views.login),
]