from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('login-user/', views.login_user, name='login-user'),
    path('register-user/', views.register_user, name='register-user'),
    path('logout-user/', views.logoutUser, name='logout-user'),
    
    #CRUD
    path('create-record/', views.createRecord, name='create-record'),
    path('view-record/<int:pk>', views.viewRecord,  name='view-record'),
    path('update-record/<int:pk>', views.updateRecord, name='update-record'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete-record/<int:pk>', views.deleteRecord, name='delete-record'),
]



