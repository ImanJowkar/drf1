from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import UserRegisterSerializer
# Create your views here.


class UserRegisterView(APIView):
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    


















