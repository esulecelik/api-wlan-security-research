import logging
from rest_framework.views import APIView
from rest_framework.response import Response


class DeauthAttackView(APIView):
    
    def get(self, request):
        return Response({"message": "Test GET"}, status=200)
    
    def post(self, request):
       return Response({"message": "Test POST"}, status=200)