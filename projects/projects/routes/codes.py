from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from projects.models import Code
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework import permissions

class CodeSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Code.objects.all())
    # project = serializers.ReadOnlyField(source='project.id')
    class Meta:
        model = Code
        fields = ['id', 'title', 'code', 'project', 'created_at', 'updated_at']

class CodeViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save()
