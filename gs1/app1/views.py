from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import json

# from rest_framework import api_views

# Create your views here.


def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type="application/json")


def student_details(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return JsonResponse(serializer.data, safe=False)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type="application/json")