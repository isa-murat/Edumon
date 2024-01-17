from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.users.models import Users, Students

class UserRegistrationSerializer(ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = Users
        fields = ['id', 'username', 'password','password2','email']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, value):
        password = value.get('password')
        password2 = value.pop('password2')

        if password != password2:
            raise serializers.ValidationError('passwords not matching')

        return value
    def create(self, validated_data):
        password = validated_data.pop('password2', None)
        user = super(UserRegistrationSerializer, self).create(validated_data)

        if password is not None:
            user.set_password(password)
            user.save()
        return user

class StudentsSerializer(ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


