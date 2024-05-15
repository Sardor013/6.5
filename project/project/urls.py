from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.get_info, name='get_info'),
    path('books/<int:pk>/', views.get_book, name='get_book'),
    path('book/<int:pk>/', views.detail, name='detail'),
    path('add/', views.add_book, name='add_book'),
    path('update/<int:pk>/', views.update_book, name='update_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    
]