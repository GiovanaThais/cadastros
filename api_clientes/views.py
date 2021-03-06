from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
#from rest_framework.authentication import TokenAuthentication 
from rest_framework import filters
from rest_framework import generics
from rest_framework.filters import SearchFilter

from api_clientes import serializers
from rest_framework.generics import get_object_or_404
from .serializers import ClientesSerializer, EnderecoSerializer

from core import models
#from .models import Cliente, Endereco


class ListarClientesViewSet(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated, )
    #authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'email'] #filtro de pesquisa

    serializer_class = ClientesSerializer
    queryset = models.Cliente.objects.all()

class ClientesAPIView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated, )
    queryset = models.Cliente.objects.all()
    serializer_class = ClientesSerializer

class ListarEnderecoAPIView(generics.ListCreateAPIView):
    queryset = models.Endereco.objects.all()
    serializer_class = EnderecoSerializer

    #permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.kwargs.get('cliente_pk'):
            return self.queryset.filter(cliente_id=self.kwargs.get('cliente_pk'))
        return self.queryset.all()

class EnderecoAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EnderecoSerializer
    queryset = models.Endereco.objects.all()
    #permission_classes = (IsAuthenticated, )
# Create your views here.
