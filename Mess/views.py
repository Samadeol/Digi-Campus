from django.shortcuts import render, redirect
from django.http import Http404,HttpResponse
from .models import messMain, messOrder,messExtras
from django.http import Http404, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import messOrderSerializer,messExtrasSerializer,messMainSerializer
from django.contrib.auth.decorators import login_required
from Login.models import Profile
from Login.views import dashboard_view
import time

# Create your views here

@login_required
def mess_view(request,*args,**kwargs):
    i=1
    context={
        "Extras_1":"",
        "Extras_2":"",
        "Extras_3":"",
        "Extras_4":"",
        "Extras_5":"",
        "Extras_6":"",
        "price_1":"",
        "price_2":"",
        "price_3":"",
        "price_4":"",
        "price_5":"",
        "price_6":"",
        "Main_1":"",
        "Main_2":"",
        "Main_3":"",
        "Main_4":"",
        "Main_5":"",
        "Main_6":"",
    }
    for object in messExtras.objects.all():
        context["Extras_"+str(i)]=  context["Extras_"+str(i)]+object.extras_1
        context["price_"+str(i)]=context["price_"+str(i)]+str(object.price_1)
        
        i=i+1
    

    i=1

    for object in messMain.objects.all():
        context["Main_"+str(i)]= context["Main_"+str(i)]+ object.main_1
        i=i+1

    if(request.user.profile.is_student==False):
        return HttpResponse("<h1>Page not found</h1>")
    return render(request,'mess.html',context)

        

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
        obj = Profile.objects.get(roll_no=serializer.data['rollno'])
        obj.expense_current = obj.expense_current+serializer.data['total']
        obj.expense_total = obj.expense_total+serializer.data['total']
        obj.order_id = serializer.data['id']
        obj.e_9 = obj.e_9 + serializer.data['total']
        print(serializer.data['total'])
        obj.save()
        #object.expense_total = object.expense_total+serializer.data['total']
        return Response(serializer.data) 
    else:
        return Response("ankurs mom")
    

@api_view(['DELETE'])
def orderDelete(request,pk):
    order = messOrder.objects.get(id=pk)
    order.delete()
    return Response('mom')

def manager_view(request,*args,**kwargs):
    if(request.user.profile.is_staff==False):
        return HttpResponse("<h1>Page not found</h1>")
    return render(request,'manager.html')

def confirm_view(request):
    object=messOrder.objects.get(id=request.user.profile.order_id)
    context={
            'Selected_1' : object.item_1,
            'Selected_2' : object.item_2,
            'Selected_3' : object.item_3,
            'Selected_4' : object.item_4,
            'Selected_5' : object.item_5,
            'Selected_6' : object.item_6,
            'Quantity_1':object.quantity_1,
            'Quantity_2':object.quantity_2,
            'Quantity_3':object.quantity_3,
            'Quantity_4':object.quantity_4,
            'Quantity_5':object.quantity_5,
            'Quantity_6':object.quantity_6,
            'Price_1':object.price_1,
            'Price_2':object.price_2,
            'Price_3':object.price_3,
            'Price_4':object.price_4,
            'Price_5':object.price_5,
            'Price_6':object.price_6,

        }
    return render(request,'new_confirm.html',context)

def cancel_view(request):
    object=messOrder.objects.get(id=request.user.profile.order_id)
    object.delete()
    request.user.profile.order_id=0
    request.user.profile.save()
    return redirect ('../')
    

# def confirm_view(request):
#     from django.http import JsonResponse
#     if request.method=='POST' and request.is_ajax():
#         try:
#            request.user.messOrder.price_1=80

            
   
#         except messOrder.DoesNotExist:
#             return JsonResponse({'status':'Fail'})

#     else:
#         return JsonResponse({'status':'Fail'})

def hash_view(request,*args,**kwargs):
    dashboard_view(request,*args,**kwargs)
    return redirect('../dashboard')    


@api_view(['GET'])
def main_menu_list(request):
    orders = messMain.objects.all().order_by('-id')
    serializer = messMainSerializer(orders, many=True)
    return Response(serializer.data) 


@api_view(['GET'])
def main_menu_detail(request,pk):
    orders = messMain.objects.get(id=pk)
    serializer = messMainSerializer(orders, many=False)
    return Response(serializer.data) 

@api_view(['POST'])
def main_menu_create(request):
    serializer = messMainSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) 
    else:
        return Response("ankurs mom")



@api_view(['DELETE'])
def main_menu_delete(request,pk):
    order = messMain.objects.get(id=pk)
    order.delete()
    return Response('mom')



@api_view(['GET'])
def main_extras_list(request):
    orders = messExtras.objects.all().order_by('-id')
    serializer = messExtrasSerializer(orders, many=True)
    return Response(serializer.data) 


@api_view(['GET'])
def main_extras_detail(request,pk):
    orders = messExtras.objects.get(id=pk)
    serializer = messExtrasSerializer(orders, many=False)
    return Response(serializer.data) 

@api_view(['POST'])
def main_extras_create(request):
    serializer = messExtrasSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) 
    else:
        return Response("ankurs mom")



@api_view(['DELETE'])
def main_extras_delete(request,pk):
    order = messExtras.objects.get(id=pk)
    order.delete()
    return Response('mom')

@login_required
def order_list_view(request):
    order=messOrder.objects.filter(rollno=request.user.profile.roll_no).order_by('-orderedDate')
    context=[]
    name=[]
    quantity=[]
    price=[]
    date=[]
    i=1
    for object in order:
        if(i>6):
            break
        i=i+1
        name.append(object.item_1)
        name.append(object.item_2)
        name.append(object.item_3)
        name.append(object.item_4)
        name.append(object.item_5)
        name.append(object.item_6)
        date.append(object.orderedDate)
        quantity.append(object.quantity_1)
        quantity.append(object.quantity_2)
        quantity.append(object.quantity_3)
        quantity.append(object.quantity_4)
        quantity.append(object.quantity_5)
        quantity.append(object.quantity_6)
        if(object.quantity_1==0):
            price.append(0)
        else:
            price.append(object.price_1*object.quantity_1)
        
        if(object.quantity_2==0):
            price.append(0)
        else:
            price.append(object.price_2*object.quantity_2)
        if(object.quantity_3==0):
            price.append(0)
        else:
            price.append(object.price_3*object.quantity_3)
        
        if(object.quantity_4==0):
            price.append(0)
        else:
            price.append(object.price_4*object.quantity_4)

        if(object.quantity_5==0):
            price.append(0)
        else:
            price.append(object.price_5*object.quantity_5)

        if(object.quantity_6==0):
            price.append(0)
        else:
            price.append(object.price_6*object.quantity_6)

        
    
        

    context={}
    
    name_1=[]
    quantity_1=[]
    price_1=[]
    date_1=[]
    
    for i in range(len(name)):
        name_1.append("Name_"+str(i))
        context[name_1[i]]=name[i]

    for i in range(len(name),36):
        name_1.append("Name_"+str(i))
        context[name_1[i]]="-"
           
    for j in range(len(quantity)):
        quantity_1.append("Quantity_"+str(j))
        context[quantity_1[j]]=quantity[j]
    
    for j in range(len(quantity),36):
        quantity_1.append("Quantity_"+str(j))
        context[quantity_1[j]]="-"

    for k in range(len(price)):
        price_1.append("Price_"+str(k))
        context[price_1[k]]=price[k]
    
    for k in range(len(price),36):
        price_1.append("Price_"+str(k))
        context[price_1[k]]="-"

    for l in range(len(date)):
        date_1.append("Date_"+str(l))
        context[date_1[l]]=date[l]

    for l in range(len(date),6):
        date_1.append("Date_"+str(l))
        context[date_1[l]]="--/--/----"

    
    

    return render(request,"order_list.html",context)

