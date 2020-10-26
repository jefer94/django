from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from projects.routes import UserViewSet, ProjectViewSet, CodeViewSet, ProjectPermissionViewSet

# Routers provide an easy way of automatically determining the URL conf.

# project_list = ProjectViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# project_detail = ProjectViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# router = routers.DefaultRouter()
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet, basename='project-list')
router.register(r'projects/1', ProjectViewSet, basename='project-detail')
router.register(r'codes', CodeViewSet, basename='codes-list')
router.register(r'codes/1', CodeViewSet, basename='codes-detail')
router.register(r'project-permission', ProjectPermissionViewSet, basename='project-permission-list')
router.register(r'project-permission/1', ProjectPermissionViewSet, basename='project-permission-detail')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('projects', project_list, name='project-list'),
    # path('projects/<int:pk>', project_detail, name='project-detail')
]
