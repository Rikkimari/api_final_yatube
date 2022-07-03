from rest_framework import serializers


class ValidateFollowing:
    """Класс принимает на вход произвольное количество полей
    и проверяет их на уникальность
    """
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, attrs):
        list_fields = []
        for i in range(len(self.fields)):
            list_fields.append(attrs[self.fields[i]])
        if len(self.fields) != len(set(list_fields)):
            raise serializers.ValidationError(
                'Нельзя подписаться на себя')
