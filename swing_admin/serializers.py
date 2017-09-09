from rest_framework.serializers import HyperlinkedModelSerializer

from swing_admin.models import News, Dates


class NewsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = (
            'created',
            'title',
            'text',
        )


class DatesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Dates
        fields = (
            'created',
            'start',
            'name',
        )
