from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Animal
from .serializers import AnimalSerializer


class AnimalListView(APIView):
    @staticmethod
    def get(request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, context={'request':request}, many=True)
        return Response(serializer.data)

class AnimalView(APIView):
    @staticmethod
    def get(request, pk):
        try:
            animal = Animal.objects.filter(pk=pk)
            serializer = AnimalSerializer(animal, context={'request': request}, many=False)
            return Response(serializer.data, status=200)
        except Animal.DoesNotExist:
            return Response('Animal does not exist', status=404)

class AddAnimalView(APIView):
    @staticmethod
    def post(request):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('animal was aded', status=201)
        else:
            return Response(serializer.errors)

class DeleteAnimalView(APIView):
    @staticmethod
    def delete(request, pk):
        try:
            animal = Animal.objects.get(pk=pk)
            animal.delete()
            return Response('Animal deleted successfully!')
        except Animal.DoesNotExist:
            return Response('animal does not exist')





















