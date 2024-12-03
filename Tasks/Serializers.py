from rest_framework import serializers

from Tasks.models import Task, Category


class TaskSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    class Meta:
        model = Task
        fields = ['id', 'title', 'category', 'description','is_done','created_at','start_date','end_date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'