from django.urls import path 
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static
from api_clientes.views import EnderecoAPIView,ListarEnderecoAPIView,ListarClientesViewSet,ClientesAPIView

from django.urls.resolvers import URLPattern 
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('cliente', ClientesAPIView)
router.register('endereco', EnderecoAPIView)

urlpatterns = [
    #urls da API
    path('cliente/', ListarClientesViewSet.as_view(), name='clientes_api'),
    path('cliente/<int:pk>/', ClientesAPIView.as_view(), name='cliente_api'),
    path('cliente/<int:cliente_pk>/endereco/', ListarEnderecoAPIView.as_view(), name='cliente_enderecos'),
    path('cliente/<int:cliente_pk>/endereco/<int:pk>/', EnderecoAPIView.as_view(), name='endereco_clientes')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)