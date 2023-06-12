from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router1 = DefaultRouter()
router1.register('', views.QuestionView)

router2 = DefaultRouter()
router2.register('', views.AnswerView)


urlpatterns = [
    path('', views.HomeView.as_view()),
    path('question/', include(router1.urls)),
    path('answer/', include(router2.urls)),
]
