from carrinho.models.carrinho import Carrinho
from carrinho.serializers.carrinho import CarrinhoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class CarrinhoItem(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, all):
        user_logado = request.user.id
        if all == 'true':
            carrinho = Carrinho.objects.filter(
                cliente=user_logado, checkout = 'true')
        elif  Carrinho.objects.filter(
            cliente = user_logado, checkout='false').last():
            carrinho = Carrinho.objects.filter(
                    checkout='false', cliente = user_logado)
        else:
            Carrinho.objects.create(
                checkout='false', 
                cliente = user_logado)
            carrinho = Carrinho.objects.filter(
                checkout='false', cliente = user_logado)
        serializer = CarrinhoSerializer(carrinho, many = True)
        return Response(serializer.data)

class CarrinhoDetailChangeDeleteGet(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get_object(self, pk):
        if Carrinho.objects.get(pk = pk):
            return Carrinho.objects.get(pk = pk)
        return Response( status = status.HTTP_404_NOT_FOUND)

    def get(self,request, pk):
        carrinho = Carrinho.objects.filter(id=pk)
        serializer = CarrinhoSerializer(carrinho, many = True)
        return Response(serializer.data)

    def put(self, request, pk):
        carrinho = Carrinho.objects.filter(pk = pk)
        if carrinho:
            carrinho = self.get_object(pk)
            serializer = CarrinhoSerializer(carrinho, data= request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(checkout = 'true')
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