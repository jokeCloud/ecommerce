from django.urls import path

from .views import Detalhe, FecharPedido, Pagar

app_name = 'pedido'

urlpatterns = [
    path('', Pagar.as_view(), name='pagar'),
    path('detalhe/', Detalhe.as_view(), name='detalhe'),
    path('fecharpedido/', FecharPedido.as_view(), name='fecharpedido'),
]
