from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class AliveView(APIView):
    """
        Endpoint used to check if our server,
        django and django-rest are up and running
    """
    
    def get(self, request):
        return Response({'alive': True}, status=status.HTTP_200_OK)
