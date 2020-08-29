import django_filters
from .models import *


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title',lookup_expr='icontains',label='Search')

    class Meta:
        model = Post
        fields = ['title']