from rest_framework import serializers


class NestedTeamSerializer(serializers.Serializer):
    id      = serializers.IntegerField()
    name    = serializers.CharField()
    icon    = serializers.CharField()
    score   = serializers.CharField()


class MatchSerializer(serializers.Serializer):
    finished    = serializers.BooleanField()
    datetime    = serializers.DateTimeField()
    team_1      = NestedTeamSerializer()
    team_2      = NestedTeamSerializer()
