from rest_framework import serializers
from django.contrib.auth.models import User



def clean_email(value:str):
    if 'admin' in value.lower():
        raise serializers.ValidationError("admin not allowed in email")


class UserRegisterSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('username','email', 'password', 'password2')    
        extra_kwargs = {
            'password':{'write_only':True},
            'email': {'validators': [clean_email]},        
        }


    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("password must be equal")
        
        return data
    
    def validate_username(self, value:str):
        if value.lower() == 'admin':
            raise serializers.ValidationError("username cannot be admin")
        return value
            
    def create(self, validated_data):
        del validated_data['password2']
        User.objects.create(**validated_data)
    