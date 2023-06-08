from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PersonSerializer
from .models import Person



# Create your views here.

class HomeView(APIView):
    def get(self, request):
        person = Person.objects.all()
        ser_data = PersonSerializer(instance=person, many=True)
        return Response(ser_data.data)
    
    def post(self, request):
        name = request.data
        return Response({'data':name}) 
