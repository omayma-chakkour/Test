from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from crudOps.models import Users
from crudOps.serializers import UsersSerializer as usersSerializer


from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def usersApi(request,id=0):
    if request.method=='GET':
        users = Users.objects.all()
        users_serializer=usersSerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)
    elif request.method=='POST':
        users_data=JSONParser().parse(request)
        users_serializer=usersSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)


    elif request.method=='PUT':
        users_data=JSONParser().parse(request)
        users=Users.objects.get(username=users_data['username'])
        users_serializer=usersSerializer(users,data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")



    elif request.method=='DELETE':
        users=Users.objects.get(id=id)
        users.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)