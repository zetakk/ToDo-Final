from django.urls import path

from accounts.views import RegisterUserView, UserLoginView, UserLogoutView, UserPasswordChangeView, UserDeleteView

urlpatterns = [
    path('register-user/', RegisterUserView.as_view(), name='register-user'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('password-change/', UserPasswordChangeView.as_view(), name='password-change'),
    path('delete-user/<int:pk>/', UserDeleteView.as_view(), name='delete-user'),
]
