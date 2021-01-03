from basic_api.models import BasicApi
from rest_framework import viewsets, permissions
from .serializers import BasicApiSerializer


class BasicApiViewSet(viewsets.ModelViewSet):
    queryset = BasicApi.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BasicApiSerializer
