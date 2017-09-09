
# Create your models here.
from django.db import models
from django.utils.timezone import now
from django_undeletable.models import BaseModel, DataManager
from froala_editor.fields import FroalaField


class News (BaseModel):
    title = models.CharField('Titel', max_length=100)
    text = FroalaField('Nachricht')

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class DatesManager(DataManager):
    def future(self):
        return self.filter(start__gt=now())


class Dates(BaseModel):
    start = models.DateTimeField('Datum')
    name = models.CharField('Veranstaltung', max_length=150)

    data = DatesManager()

    class Meta:
        verbose_name = 'Date'
        verbose_name_plural = 'Dates'
        ordering = ['start']

    def __str__(self):
        return self.name
