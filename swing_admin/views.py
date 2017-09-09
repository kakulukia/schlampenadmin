from django.shortcuts import render


# Create your views here.
from rest_framework.viewsets import ModelViewSet

from swing_admin.models import News, Dates
from swing_admin.serializers import NewsSerializer, DatesSerializer


def index(request):
    return render(request, 'index.pug')


class NewsViewSet(ModelViewSet):
    queryset = News.data.all()
    serializer_class = NewsSerializer


class DatesViewSet(ModelViewSet):
    queryset = Dates.data.future()
    serializer_class = DatesSerializer
