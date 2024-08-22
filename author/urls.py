from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    # path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('edit/pass-change/', views.pass_change, name='pass_change'),
]
