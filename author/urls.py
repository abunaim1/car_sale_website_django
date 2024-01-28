from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signUp, name='signUp'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit, name='edit'),
    path('logout/', views.user_logout , name='logout')
]
