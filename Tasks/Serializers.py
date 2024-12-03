from rest_framework import serializers

from Tasks.models import Task, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    category = serializers.CharField(read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'category', 'description','is_done','created_at','start_date','end_date']