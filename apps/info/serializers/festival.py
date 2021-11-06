from rest_framework import serializers

from apps.info.models import Festival


class FestivalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Festival
        exclude = ("created", "modified")


class FestivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Festival
        fields = ("year",)
