from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.exceptions import ValidationError

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer