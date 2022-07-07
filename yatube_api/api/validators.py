from rest_framework import serializers


class ValidateFollowing:
    """Класс принимает на вход произвольное количество полей
    и проверяет их на уникальность
    """
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, attrs):
        checked_field = [attrs[field] for field in self.fields]
        if len(self.fields) != len(set(checked_field)):
            raise serializers.ValidationError(
                'Нельзя подписаться на себя')
