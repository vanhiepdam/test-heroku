# -*- coding: utf-8 -*-
from django.db import models

from prepare_be.models import TrackingAbstractModel


class Todo(TrackingAbstractModel):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
