from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from .serializers import QuokkaSerializer
from .models import Quokka
import random
import json

# Create your views here.
@api_view(['GET'])
def quokka_api(request):    
    imgurl = Quokka.objects.all()
    randint = random.randint(0, len(imgurl))
    serializer = QuokkaSerializer(imgurl[randint])
    return Response(serializer.data)

@api_view(['GET'])
def setdata(request):
    lst = Quokka.objects.all()
    for tmp in lst:
        tmp.delete()

    url = "https://sheets.googleapis.com/v4/spreadsheets/13JMJ-z_cFgJRS0JHgmhb_vYPqbtVu4189Ey24g5OA9A/values/sheet1?key=AIzaSyA0lUwKXrKqbArUtmjv0un3KSBGemrlwl0"
    response = requests.get(url)
    response = json.loads(response.text)
    ress = response['values']

    for res in ress:
        tmp = res[0][5:]
        lst = {'data' : tmp}
        serializer = QuokkaSerializer(data=lst)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return Response('delete')