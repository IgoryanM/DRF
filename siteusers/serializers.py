from rest_framework.serializers import HyperlinkedModelSerializer
from .models import SiteUsers


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = SiteUsers
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email', 'age')


class UserModelSerializerWithSuStaff(HyperlinkedModelSerializer):
    class Meta:
        model = SiteUsers
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email', 'age', 'is_superuser', 'is_staff')
