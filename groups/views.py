from rest_framework.views import APIView, Response, status
from .models import Animal
from .serializers import AnimalSerializer
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

