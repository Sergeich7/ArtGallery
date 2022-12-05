from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
        label='Username', max_length=128, required=True)
    email = serializers.EmailField(
        label='Email', max_length=128, required=True)
    password = serializers.CharField(
        label='Password', max_length=128, write_only=True, required=True)

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model()(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ChangeUserPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        label='Old password', max_length=128, write_only=True, required=True)
    new_password1 = serializers.CharField(
        label='New Password', max_length=128, write_only=True, required=True)
    new_password2 = serializers.CharField(
        label='Repeat new password', max_length=128,
        write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                ('Your old password was entered incorrectly. Please enter it again.')
            )
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError(
                {'new_password2': ("The two password fields didn't match.")})
        validate_password(data['new_password1'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user
