from accounts.models import CustomUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'following']
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

# class CustomUserSerializer(serializers.ModelSerializer):
#     class meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'bio', 'profile_picture']
        
# class RegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(max_length=255, write_only=True)
    
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password1', 'password2']
        
#     def validate(self, attrs):
#         if attrs['password1'] != attrs['ppassword2']:
#             raise serializers.ValidationError({'password': 'password do not match.'})
#         return attrs
    
# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password']