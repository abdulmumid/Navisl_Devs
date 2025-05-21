from rest_framework import serializers
from .models import Service, ContactRequest, About, Panel, Tool, Project, Review, Consult, Dizain, Image, Job, JobApplication

import re
from django import forms



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'




class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = ['id', 'phone', 'email', 'created_at']
        read_only_fields = ['id', 'created_at']

class PanelSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()

    class Meta:
        model = Panel
        fields = '__all__'

    def get_features(self, obj):
        return obj.get_features_list()


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'

    def get_features(self, obj):
        return obj.get_features_list()
    
class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consult
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
            'text': forms.Textarea(attrs={'placeholder': 'Что вас интересует?', 'rows': 3}),
        }

class DizainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dizain
        fields = '__all__'
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
