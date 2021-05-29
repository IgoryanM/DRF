from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Project, Note
from .serializers import ProjectModelSerializer, NoteModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilter, DataFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class NoteLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter


class NoteModelViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteModelSerializer
    pagination_class = NoteLimitOffsetPagination
    filterset_class = DataFilter
    filterset_fields = ['project']

    def destroy(self, request, pk=None, *args, **kwargs):
        note = get_object_or_404(Note, pk=pk)
        note.is_active = False
        note.save()
        serializer = self.get_serializer(note)
        return Response(serializer.data)
