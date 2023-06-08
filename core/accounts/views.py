from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import UserRegisterSerializer
# Create your views here.


class UserRegisterView(APIView):
    
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            User.objects.create(
                username = ser_data.validated_data['username'],
                email = ser_data.validated_data['email'],
                password = ser_data.validated_data['password1'],
            )
            return Response(ser_data.data, status.HTTP_201_CREATED)
        return Response(ser_data.errors, status.HTTP_400_BAD_REQUEST)
    


















