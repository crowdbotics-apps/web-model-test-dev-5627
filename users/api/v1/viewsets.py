from rest_framework import authentication
from users.models import HJGhjkh
from .serializers import HJGhjkhSerializer
from rest_framework import viewsets


class HJGhjkhViewSet(viewsets.ModelViewSet):
    serializer_class = HJGhjkhSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = HJGhjkh.objects.all()
