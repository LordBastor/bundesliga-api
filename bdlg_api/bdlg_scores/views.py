# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bdlg_main.main_view import BDLGBaseView

from rest_framework import status
from rest_framework.response import Response

from .serializers import ScoreSerializer


class TeamScoreListView(BDLGBaseView):
    def get(self, request):
        """
            Returns a list of all teams in the league and their score
            
            Response code: 200
            
            Response body: ScoreSerializer
            ---
            
            serializer: ScoreSerializer
        """
        scores = self.wrapper.get_scores()
        serializer = ScoreSerializer(scores, many=True)
        return self.get_mocked_pagination_response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )


class TeamScoreDetailView(BDLGBaseView):
    def get(self, request, team_id):
        """
            Returns the scores of a specific team by its id
            
            Response code: 200
            
            Response body: ScoreSerializer
            ---
            
            serializer: ScoreSerializer
        """
        score = self.wrapper.get_team_score(int(team_id))
        serializer = ScoreSerializer(score)
        return self.get_mocked_pagination_response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
