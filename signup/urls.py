from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name='sign_up'),
    path('login/', views.user_login, name='login'),
    path('user_profile/', views.profile, name='user_profile'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('pass-change/', views.pass_change, name='pass_change'),
    path('pass-change-two/', views.pass_change2, name='pass_change_two'),
]
