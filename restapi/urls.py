from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from siteusers.views import UserCustomViewSet
from todo_app.views import ProjectModelViewSet, NoteModelViewSet

router = DefaultRouter()
#router.register('users', UserModelViewSet)
router.register('users', UserCustomViewSet)
router.register('projects', ProjectModelViewSet)
router.register('notes', NoteModelViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   path('api/', include(router.urls)),
]

