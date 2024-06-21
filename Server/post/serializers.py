from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Vacancy, Comment, Publication

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['employer', 'title', 'description', 'requirements', 'salary', 'location', 'employment_type']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'employer', 'vacancy', 'content']

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['user', 'title', 'content']