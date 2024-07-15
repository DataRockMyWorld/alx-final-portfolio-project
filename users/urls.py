from django.urls import path
from .views import register, login_view, approve_user, user_list, dashboard, account
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('approve_user/<int:user_id>/', approve_user, name='approve_user'),
    path('user_list/', user_list, name='user_list'),
    path('dashboard/', dashboard, name='dashboard'),
    path('account/', account, name='account'),
]
