from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from siteusers.views import UserCustomViewSet
from todo_app.views import ProjectModelViewSet, NoteModelViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="ToDo_app",
        default_version='1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('users', UserCustomViewSet)
router.register('projects', ProjectModelViewSet)
router.register('notes', NoteModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/<str:version>/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
