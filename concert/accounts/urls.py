from django.urls import path
from accounts import views

urlpatterns = [    
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'), 
    path('profile/', views.profileView, name='profile'),   
    path('profileRegister/', views.profileRegisterView, name='profileRegister'),
    path('profileEdit/', views.ProfileEditView, name='profileEdit'),  
]
