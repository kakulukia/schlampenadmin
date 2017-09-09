
# Register your models here.
from django.contrib.admin import register
from django.contrib.admin.options import ModelAdmin

from swing_admin.models import Dates, News


@register(Dates)
class DatesAdmin(ModelAdmin):
    list_display = [
        'start',
        'name',
    ]
    actions = None


@register(News)
class NewsAdmin(ModelAdmin):
    list_display = [
        'created',
        'title',
    ]
    actions = None
