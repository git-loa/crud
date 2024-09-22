from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('login-user/', views.login_user, name='login-user'),
    path('register-user/', views.register_user, name='register-user'),
    path('create-record/', views.createRecord, name='create-record'),
    path('update-record/', views.updateRecord, name='update-record'),
    path('view-record/', views.viewRecord,  name='view-record'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout-user/', views.logoutUser, name='logout-user'),
]