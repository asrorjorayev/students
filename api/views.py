from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import AllStudentsSerializerView


class AllStudentsView(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=AllStudentsSerializerView(students,many=True)

        return Response(data=serializer.data)
    def post(self,request):

        serializer=AllStudentsSerializerView(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
class StudentView(APIView):
    def get(self,request,id):
        student=Student.objects.get(id=id)
        serializer=AllStudentsSerializerView(student)

        return Response(data=serializer.data)
    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = AllStudentsSerializerView(student, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        
   
     


        
