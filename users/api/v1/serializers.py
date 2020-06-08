from rest_framework import serializers
from users.models import HJGhjkh


class HJGhjkhSerializer(serializers.ModelSerializer):
    class Meta:
        model = HJGhjkh
        fields = "__all__"
