# views.py
from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']  # Enables filtering by 'status' using ?status=...
    search_fields = ['title', 'description']  # Enables searching using ?search=...
    
    @action(detail=False, methods=['get'])
    def overdue(self, request):
        today = timezone.now().date()
        overdue_tasks = self.queryset.filter(due_date__lt=today)
        serializer = self.get_serializer(overdue_tasks, many=True)
        return Response(serializer.data)
