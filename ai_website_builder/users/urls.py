# from django.urls import path
# from .views import RegisterView, LoginView

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
# ]

from django.urls import path
from .views import register_view, login_view,refresh_token
from .api_views import RegisterAPIView, LoginAPIView

app_name = 'users'

urlpatterns = [
    # Frontend form routes
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),

    # API endpoints
    path('api/register/', RegisterAPIView.as_view(), name='api_register'),
    path('api/login/', LoginAPIView.as_view(), name='api_login'),
    path('refresh/', refresh_token, name='refresh_token'),  # Add this line

]
