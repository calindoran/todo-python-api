from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)


class GetUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        user_data = []
        for user in users:
            user_data.append({
                "id": user.id,
                "name": user.username,
                "name": user.name,
                "email": user.email
            })
        return Response(user_data, status=status.HTTP_200_OK)
