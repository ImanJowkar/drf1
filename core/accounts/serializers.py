from rest_framework import serializers




def clean_email(value:str):
    if 'admin' in value.lower():
        raise serializers.ValidationError("admin not allowed in email")


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[clean_email])
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    
    
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("password must be equal")
        
        return data
    
    def validate_username(self, value:str):
        if value.lower() == 'admin':
            raise serializers.ValidationError("username cannot be admin")
        return value
            
    