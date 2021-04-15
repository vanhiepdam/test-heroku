from rest_framework import serializers

from todo.models.todo import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id',
            'title',
            'description',
            'completed',
        )
