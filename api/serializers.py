from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import UserProfile, UserPreferences


class UserSerializer(serializers.ModelSerializer):
    """
    Serializator usera, gdy żądanie jest typu GET password jest usuwane z serializacji
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        up = UserProfile.objects.create(user=user)
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializator profilu usera, dopuszczalna edycja avatara
    """

    class Meta:
        model = UserProfile
        fields = ('user', 'picture', 'created',)
        read_only_fields = ('user',)

