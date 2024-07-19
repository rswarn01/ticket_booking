from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "phone_number",
            "address",
            "password",
        ]

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            phone_number=validated_data["phone_number"],
            address=validated_data["address"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
