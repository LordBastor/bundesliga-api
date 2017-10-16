# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bdlg_main.main_view import BDLGBaseView

from rest_framework import status
from rest_framework.response import Response

from .serializers import MatchSerializer

class UpcomingMatchView(BDLGBaseView):
    def get(self, request):
        """
            Returns a list of all upcoming matches
            
            Response code: 200
            
            Response body: MatchSerializer
            ---
            
            serializer: MatchSerializer
        """
        upcoming_matches = self.wrapper.get_upcoming_matches()
        serializer = MatchSerializer(upcoming_matches, many=True)
        return self.get_mocked_pagination_response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )


class UpcomingMatchTeamView(BDLGBaseView):
    def get(self, request, team_id):
        """
            Returns a list of all upcoming matches
            for a given match by team_id
            
            Response code: 200
            
            Response body: MatchSerializer
            ---
            
            serializer: MatchSerializer
        """
        upcoming_matches = self.wrapper.get_team_matches(team_id)
        serializer = MatchSerializer(upcoming_matches, many=True)
        return self.get_mocked_pagination_response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )


class AllMatchView(BDLGBaseView):
    def get(self, request):
        """
            Returns a list of all matches
            
            Response code: 200
            
            Response body: MatchSerializer
            ---
            
            serializer: MatchSerializer
        """
        all_matches = self.wrapper.get_all_matches_digested()
        serializer = MatchSerializer(all_matches, many=True)
        return self.get_mocked_pagination_response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
