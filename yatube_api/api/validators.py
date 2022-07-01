from rest_framework import serializers


class ValidateFollowing:

    def __init__(self, user_field='user', following_field='following'):
        self.user_field = user_field
        self.following_field = following_field

    def __call__(self, attrs):
        if attrs[self.user_field] == attrs[self.following_field]:
            raise serializers.ValidationError(
                'Нельзя подписаться на себя')
