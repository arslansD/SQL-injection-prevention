# api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User
from django.db import connection

class UserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Use parameterized query to prevent SQL injection
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM api_user WHERE username = %s AND password = %s", (username, password))
            results = cursor.fetchall()

        return Response(results)
