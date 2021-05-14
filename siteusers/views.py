from rest_framework.viewsets import ModelViewSet
from .models import SiteUsers
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = SiteUsers.objects.all()
    serializer_class = UserModelSerializer
