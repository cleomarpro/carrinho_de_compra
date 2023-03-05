from .serializers import UsuarioSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.permissions import IsAuthenticated 

class NovoUsuario(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_BAD_CREATED)

class NovaSenha(APIView):
    def get(self, request):
        user_id = request.user.id
        user = User.objects.filter(id = user_id)
        serializer = UsuarioSerializer(user, many = True)
        return Response(serializer.data)

    def put(self, request):
        serializer = UsuarioSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)