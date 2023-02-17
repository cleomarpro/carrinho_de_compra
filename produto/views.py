from produto.models import Produto
from produto.serializers import ProdutoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.exceptions import NotFound
#from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated 

class ProdutoFiltro( APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, filtro='score'):
        if filtro == 'score':
            produto = Produto.objects.all().order_by(F'-{filtro}')
        elif filtro == 'price':
            produto = Produto.objects.all().order_by(F'-{filtro}')
        elif filtro == 'name':
            produto = Produto.objects.all().order_by(F'{filtro}')
        else:
            produto = Produto.objects.all()
        serializer = ProdutoSerializer(produto, many = True)
        return Response(serializer.data)

class ProdutoCreate( APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        produto = Produto.objects.all()
        serializer = ProdutoSerializer(produto, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ProdutoSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_BAD_CREATED)

class ProdutoDetailChangeDelete(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        if Produto.objects.get(pk = pk):
            return Produto.objects.get(pk = pk)
        return Response( status = status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        produto = Produto.objects.filter(pk = pk)
        if produto:
            produto = self.get_object(pk)
            serializer = ProdutoSerializer(produto)
            return Response(serializer.data)
        return Response( status = status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        produto = Produto.objects.filter(pk = pk)
        if produto:
            produto = self.get_object(pk)
            serializer = ProdutoSerializer(produto, data= request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response( status = status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        produto = Produto.objects.filter(pk = pk)
        if produto:
            produto = self.get_object(pk)
            produto.delete()
            return Response(status = status.HTTP_200_OK)
        return Response( status = status.HTTP_404_NOT_FOUND)