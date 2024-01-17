from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
    drink = Drink.objects.all() # data from db
    serializer = DrinkSerializer(drink,many=True) # to convert to Json data
    return JsonResponse({"drinks" : serializer.data},safe=False)