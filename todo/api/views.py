from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from todo.models import TODOO
from .serializers import TodoSerializer
from rest_framework import viewsets,response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permissions import IsOwnerOrReadOnly


class TodoModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = TodoSerializer
    def get_queryset(self):
        # Return only the todos belonging to the authenticated user
        return TODOO.objects.filter(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return response.Response(
                {"message": "You do not have any todos yet!"},
                status=200
            )
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = {
        "title": ["in", "exact"],
        "status": ["exact"]
    }
    search_fields = ['title']
    ordering_fields = ['date']



