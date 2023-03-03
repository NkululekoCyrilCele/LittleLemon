from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu_list_create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu_detail'),
    path('menu/items/', views.MenuItemView.as_view(),
         {'post': 'create'}, name='menu_create'),
]
