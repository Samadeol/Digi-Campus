from django.shortcuts import render
from .models import messMenu, messOrder
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

@api_view(['GET'])
def orderlist(request):
    orders = messOrder.objects.all()
    serializer = messOrderSerializer(orders, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def orderDetail(request,pk):
    orders = messOrder.objects.get(id=pk)
    serializer = messOrderSerializer(orders, many=False)
    return Response(serializer.data) 

@api_view(['POST'])
def orderCreate(request):
    serializer = messOrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

@api_view(['DELETE'])
def orderDelete(request,pk):
    order = messOrder.objects.get(id=pk)
    order.delete()
    return Response('mom')

def confirm_view(request):
    from django.http import JsonResponse
    if request.method=='POST' and request.is_ajax():
        try:
           request.user.messOrder.price_1=80

            
   
        except messOrder.DoesNotExist:
            return JsonResponse({'status':'Fail'})

    else:
        return JsonResponse({'status':'Fail'})
    
    

