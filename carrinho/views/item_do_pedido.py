from carrinho.models.carrinho import Carrinho
from carrinho.models.item_do_pedido import ItemDoPedido
from carrinho.serializers.item_do_pedido import ItemDoPedidoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class ItemDoPedidoCreate( APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request,):
        user_logado = request.user.id
        carrinho = Carrinho.objects.filter(cliente=1).last()
        item = ItemDoPedido.objects.filter(carrinho_id = carrinho.id)
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
