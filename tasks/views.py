from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.utils import timezone

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['status']

    @action(detail=False, methods=['get'])
    def overdue(self, request):
        today = timezone.now().date()
        overdue_tasks = self.queryset.filter(due_date__lt=today)
        serializer = self.get_serializer(overdue_tasks, many=True)
        return Response(serializer.data)
