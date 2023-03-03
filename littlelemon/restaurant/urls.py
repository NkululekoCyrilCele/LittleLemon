from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu_list_create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu_detail'),
    path('menu/items/', views.MenuItemView.as_view(),
         {'post': 'create'}, name='menu_create'),
    path('api-token-auth/', obtain_auth_token),
]
