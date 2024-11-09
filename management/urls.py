# from django.contrib import admin
from django.urls import path
from management import views
urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('add/', views.add, name = 'add'),
    path('update/<int:pk>', views.update, name = 'update'),
    path('history/', views.history, name = 'history'),
    path('delete/<int:pk>', views.delete,name ='delete'),
    path('', views.register, name = 'register' ),
    path('login/', views.login_user, name = 'login'), 
    path('logout/', views.logout_user, name = 'logout')
]
