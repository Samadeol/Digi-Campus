from django.shortcuts import render
from .models import messMenu
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import messOrderSerializer
# Create your views here.
def mess_view(request,*args,**kwargs):
    return render(request,"mess.html",{'BDMR':'50'})

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/'
    }
    return Response(api_urls)

