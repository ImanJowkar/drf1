from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Person, Question, Answer



# Create your views here.

class HomeView(APIView):
    
    permission_classes = [IsAuthenticated, ]
    permission_classes = [IsAdminUser, ]
    def get(self, request):
        person = Person.objects.all()
        ser_data = PersonSerializer(instance=person, many=True)
        return Response(ser_data.data)
    
    def post(self, request):
        name = request.data
        return Response({'data':name}) 



class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer