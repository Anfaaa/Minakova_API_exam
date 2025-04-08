from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    
    def validate_status(self, value):
        allowed = ['new', 'in_progress', 'done']
        if value not in allowed:
            raise serializers.ValidationError("Статус должен быть: new, in_progress или done")
        return value