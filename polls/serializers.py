from rest_framework import serializers
from .models import Question


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'pub_date', 'question_text', 'was_published_recently']


class QuestionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'pub_date', 'question_text']
