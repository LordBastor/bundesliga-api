from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from bdlg_main.open_league_wrapper import OpenLeagueWrapper


class AliveView(APIView):
    """
        Endpoint used to check if our server,
        django and django-rest are up and running
    """
    
    def get(self, request):
        open_league = OpenLeagueWrapper()
        team_matches = open_league.get_team_matches(131)
        for match in team_matches:
            print match
        return Response({'alive': True}, status=status.HTTP_200_OK)
