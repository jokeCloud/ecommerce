from django.urls import path

from .views import Detalhe, Pagar, SalvarPedido

app_name = 'pedido'

urlpatterns = [
    path('', Pagar.as_view(), name='pagar'),
    path('detalhe/', Detalhe.as_view(), name='detalhe'),
    path('salvarpedido/', SalvarPedido.as_view(), name='salvarpedido'),
]
