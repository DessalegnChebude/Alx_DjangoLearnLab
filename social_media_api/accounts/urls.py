from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, ProfileViewSet, CustomTokenObtainPairView
# from .views import RegisterView, LoginView, ProfileView
from rest_framework import viewsets


#  For view set configurations is the below used
router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = [
    # path('register/', RegisterView.as_view()),
    # path('login/', LoginView.as_view, name='login'),
    # path('profile/', ProfileView.as_view, name='profile')
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
]