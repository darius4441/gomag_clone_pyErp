# Localfolder Library
from ..models.usercustom import PyUser

# Thirdparty Library
from rest_framework import serializers


class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = PyUser
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "date_joined",
        )
