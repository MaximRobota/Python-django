from django.http import HttpResponse
from .models import Question, Choice
from .serializers import QuestionListSerializer, QuestionDetailsSerializer, ChoiceListSerializer,\
    ChoiceDetailsSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer


class QuestionDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailsSerializer

    def get_object(self):
        return get_object_or_404(Question, pk=self.kwargs.get('question_id'))


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceListSerializer


class ChoiceDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChoiceDetailsSerializer

    def get_object(self):
        return get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
