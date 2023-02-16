from carrinho.models import ItemDoPedido, Carrinho
from carrinho.serializers import ItemDoPedidoSerializer, CarrinhoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.exceptions import NotFound
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class ItemDoPedidoCreate( APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        item = ItemDoPedido.objects.all()
        serializer = ItemDoPedidoSerializer(item, many = True)
        return Response(serializer.data)

    def post(self, request):
        user_logado = request.user.id
        carrinho = Carrinho.objects.filter(cliente=user_logado).last()
        serializer = ItemDoPedidoSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(carrinho = carrinho)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_BAD_CREATED)

class ItemDoPedidoDetailChangeDelete(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        if ItemDoPedido.objects.get(pk = pk):
            return ItemDoPedido.objects.get(pk = pk)
        return Response( status = status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        item = ItemDoPedido.objects.filter(pk = pk)
        if item:
            item = self.get_object(pk)
            serializer = ItemDoPedidoSerializer(item)
            return Response(serializer.data)
        return Response( status = status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        item = ItemDoPedido.objects.filter(pk = pk)
        if item:
            item = self.get_object(pk)
            serializer = ItemDoPedidoSerializer(item, data= request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response( status = status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        item = ItemDoPedido.objects.filter(pk = pk)
        if item:
            item = self.get_object(pk)
            item.delete()
            return Response(status = status.HTTP_200_OK)
        return Response( status = status.HTTP_404_NOT_FOUND)

class CarrinhoItem(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        item = ItemDoPedido.objects.filter(carrinho_id = pk)
        serializer = ItemDoPedidoSerializer(item, many = True)
        return Response(serializer.data)

    def post(self, request):
        user_logado = request.user.id
        carrinho = Carrinho.objects.filter(cliente=user_logado).last()
        serializer = ItemDoPedidoSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(carrinho = carrinho)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_BAD_CREATED)

class CarrinhoCompras(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request, checkout):
        user_logado = request.user.id
        if Carrinho.objects.filter(cliente=user_logado):
            carrinho = Carrinho.objects.filter(cliente=user_logado).last()
            if checkout != True:
                carrinho.id = carrinho.id
                carrinho.checkout = checkout
                carrinho.save()
                Carrinho.objects.create(cliente=user_logado)
        else:
            Carrinho.objects.create(cliente=user_logado)
        carrinho = Carrinho.objects.filter(cliente=user_logado).order_by('-id')
        serializer = CarrinhoSerializer(carrinho, many = True)
        return Response(serializer.data)

    def put(self, request, pk):
        carrinho = Carrinho.objects.filter(pk = pk)
        if carrinho:
            carrinho = self.get_object(pk)
            serializer = CarrinhoSerializer(carrinho, data= request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response( status = status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        carrinho = Carrinho.objects.filter(pk = pk)
        if carrinho:
            carrinho = self.get_object(pk)
            carrinho.delete()
            return Response(status = status.HTTP_200_OK)
        return Response( status = status.HTTP_404_NOT_FOUND)