from rest_framework.views import APIView, Response, status
from .models import Animal
from .serializers import AnimalSerializer
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

class AnimalView(APIView):
    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, _):
        all_animals = Animal.objects.all()

        serializer = AnimalSerializer(all_animals, many=True)

        return Response(serializer.data)

class AnimalDetailView(APIView):
    def patch(self, request, animal_id):
        animal = get_object_or_404(Animal, pk=animal_id)

        try:
            serializer = AnimalSerializer(animal, request.data, partial=True)
            serializer.is_valid(raise_exception=True)

            serializer.save()

            return Response(serializer.data)
        
        except ValidationError as e:
            return Response(e.args[0], status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self, _, animal_id):
        animal = get_object_or_404(Animal, pk=animal_id)

        serializer = AnimalSerializer(animal)

        return Response(serializer.data)

    def delete(self, _, animal_id):
        animal = get_object_or_404(Animal, pk=animal_id)

        animal.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
