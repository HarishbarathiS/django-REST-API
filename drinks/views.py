from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def drink_list(request):
    if request.method == 'GET':
        drink = Drink.objects.all() # data from db
        serializer = DrinkSerializer(drink,many=True) # to convert to Json data
        return JsonResponse({"drinks" : serializer.data},safe=False)

    if request.method == 'POST':
        serializer = DrinkSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)