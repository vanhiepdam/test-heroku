# -*- coding: utf-8 -*-
from rest_framework import routers
from django.urls import path, include
from todo.apis.v1.todo import TodoViewset

router = routers.DefaultRouter()
router.register(r'todos', TodoViewset, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
]
