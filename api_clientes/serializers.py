from rest_framework import serializers
from core import models
#from .models import Endereco


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Endereco
        fields = '__all__'