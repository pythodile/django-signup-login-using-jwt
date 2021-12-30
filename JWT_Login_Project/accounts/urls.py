from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import SignUpAPIView,LoginAPI,LogoutAPI

urlpatterns = [
    path('signup/', SignUpAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/',LoginAPI.as_view()),
    path('logout/',LogoutAPI.as_view())
    
]