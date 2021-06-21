import graphene
from graphene_django import DjangoObjectType
from siteusers.models import SiteUsers
from todo_app.models import Project, Note


class SiteUserType(DjangoObjectType):
    class Meta:
        model = SiteUsers
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class NoteType(DjangoObjectType):
    class Meta:
        model = Note
        fields = '__all__'


class Query(graphene.ObjectType):
    all_site_users = graphene.List(SiteUserType)
    all_projects = graphene.List(ProjectType)
    all_notes = graphene.List(NoteType)

    def resolve_all_site_users(root, info):
        return SiteUsers.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_notes(root, info):
        return Note.objects.all()


schema = graphene.Schema(query=Query)
