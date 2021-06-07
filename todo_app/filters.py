from datetime import timedelta

import django_filters
from django.utils import timezone
from django_filters import rest_framework as filters
from .models import Project, Note


class ProjectFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['title']


class DataFilter(django_filters.FilterSet):
    hours = django_filters.NumberFilter(
        field_name='created', method='get_past_n_hours', label="Заметки за последние N часов")

    def get_past_n_hours(self, queryset, field_name, value):
        time_threshold = timezone.now() - timedelta(hours=int(value))
        print(time_threshold, timezone.now(), timedelta(hours=int(value)))
        return queryset.filter(created__gte=time_threshold)

    class Meta:
        model = Note
        fields = ['created', ]
