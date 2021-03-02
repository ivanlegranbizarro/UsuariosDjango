from django.urls import path
from . import views
app_name = 'users_app'

urlpatterns = [
    path('user-register/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views.LoginUser.as_view(), name='login_user'),
    path('logout/', views.LogOut.as_view(), name='logout-user'),
    path('update/', views.UpdatePasswordView.as_view(), name='update_password'),
]
