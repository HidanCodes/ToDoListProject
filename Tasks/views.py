from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Tasks.Serializers import TaskSerializer, CategorySerializer
from Tasks.models import Task, Category


# Create your views here.
class getTasks(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class getDetails(APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response("No task found",status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

class addTask(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)

class updateTask(APIView):
    def put(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response("No task found",status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)

class deleteTask(APIView):
    def delete(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response("task deleted!",status=status.HTTP_204_NO_CONTENT)

class getCategories(APIView):
    def get(self, request):
        serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response(serializer.data)

class addCategory(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)