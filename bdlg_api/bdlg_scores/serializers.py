from rest_framework import serializers


class ScoreSerializer(serializers.Serializer):
    id      = serializers.IntegerField()
    name    = serializers.CharField()
    icon    = serializers.CharField()
    wins    = serializers.IntegerField()
    draws   = serializers.IntegerField()
    losses  = serializers.IntegerField()
    points  = serializers.IntegerField()
