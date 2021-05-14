from rest_framework.serializers import HyperlinkedModelSerializer
from .models import SiteUsers


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = SiteUsers
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'age')
