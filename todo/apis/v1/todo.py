# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet

from todo.models.todo import Todo
from todo.serializers.v1.todo_serializer import TodoSerializer


class TodoViewset(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
