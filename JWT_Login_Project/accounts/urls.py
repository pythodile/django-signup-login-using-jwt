from django.urls import path
from .views import SignUpAPIView,TokenAuthenticationView,TestAPI
from rest_framework.authtoken import views


urlpatterns = [
    path('signup/', SignUpAPIView.as_view()),
    path('get-token/',views.obtain_auth_token,name='get-token'),
    path('login/',TokenAuthenticationView.as_view(), name = 'login'),
    path('test/',TestAPI.as_view())
    
]