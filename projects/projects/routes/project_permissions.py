from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from projects.models import ProjectPermission
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework import permissions

class ProjectPermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectPermission
        fields = ['id', 'write', 'create', 'delete', 'project', 'user', 'created_at', 'updated_at']

class ProjectPermissionViewSet(viewsets.ModelViewSet):
    queryset = ProjectPermission.objects.all()
    serializer_class = ProjectPermissionSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save()
