from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from ..models.user import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "password", "phone")

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            phone=validated_data.get("phone", ""),
        )


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        from rest_framework_simplejwt.tokens import RefreshToken

        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except Exception:
            self.fail("bad_token")
