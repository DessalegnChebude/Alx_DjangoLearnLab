from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from .serializers import CustomUserSerializer, RegisterSerializer, CustomTokenObtainPairSerializer

# Define the views for user registration, login, and token retrieval
from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.authtoken.views import ObtainAuthToken
# from .serializers import CustomUserSerializer, RegistrationSerializer, LoginSerializer


# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomUserSerializer
    
class RegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User registered successfully."
        }, status=status.HTTP_201_CREATED)
        
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

# class RegisterView(APIView):
#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({'message': 'user created successfully.'})
#         return Response(serializer.errors, status=400)

# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data('user')
#             token, created = ObtainAuthToken.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         return Response(serializer._errors, status=400)

# class ProfileView(APIView):
#         def get(self, request):
#             user = request.user
#             serializer = CustomUserSerializer(user)
#             return Response(serializer.data)