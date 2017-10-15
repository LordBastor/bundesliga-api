from django.http import Http404
from collections import OrderedDict

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from bdlg_main.open_league_wrapper import OpenLeagueWrapper


class BDLGBaseView(APIView):
    model = None
    wrapper = OpenLeagueWrapper()
    
    def get_mocked_pagination_response(self, data=None, status=status.HTTP_200_OK, extra_meta=None):
        if isinstance(data, (list, tuple)):
            wrapped_data = []
            if isinstance(extra_meta, dict):
                wrapped_data += [(k, v) for k, v in extra_meta.iteritems()]
            wrapped_data += [
                ('count', len(data)),
                ('next', None),
                ('previous', None),
                ('results', data)
            ]
            return Response(OrderedDict(wrapped_data))
        
        if isinstance(extra_meta, dict):
            data.update(extra_meta)
        return Response(data=data, status=status)
