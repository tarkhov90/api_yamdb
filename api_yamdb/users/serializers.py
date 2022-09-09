import random
from rest_framework import serializers

from .models import User


CONFIRM_CODE_MIN = 000000
CONFIRM_CODE_MAX = 999999


def generate_confirmation_code():
    return random.randint(
        CONFIRM_CODE_MIN, CONFIRM_CODE_MAX
    )


class ConfirmationCodeGenerator:
    requires_context = False

    def __call__(self):
        return generate_confirmation_code()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email',
            'first_name', 'last_name',
            'bio', 'role',
        )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                ['Using "me" as username is forbidden.']
            )
        return value
