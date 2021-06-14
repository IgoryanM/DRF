from rest_framework import mixins, viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from .models import SiteUsers
from .serializers import UserModelSerializer, UserModelSerializerWithSuStaff


class UserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    queryset = SiteUsers.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserModelSerializerWithSuStaff
        if self.request.version == 'v1':
            return UserModelSerializer

