from rest_framework import mixins, viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from .models import SiteUsers
from .serializers import UserModelSerializer


# class UserModelViewSet(ModelViewSet):
#     queryset = SiteUsers.objects.all()
#     serializer_class = UserModelSerializer

class UserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    queryset = SiteUsers.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
