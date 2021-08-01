from django.shortcuts import render
from rest_framework import viewsets
from .models import dicts
from .serializers import dict_serializers

class dict_view(viewsets.ModelViewSet):
    queryset=dicts.objects.all()
    serializer_class=dict_serializers


