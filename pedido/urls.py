from django.urls import path

from .views import Detalhe, Lista, Pagar, SalvarPedido

app_name = 'pedido'

urlpatterns = [
    path('pagar/<int:pk>', Pagar.as_view(), name='pagar'),
    path('detalhe/<int:pk>', Detalhe.as_view(), name='detalhe'),
    path('lista/', Lista.as_view(), name='lista'),
    path('salvarpedido/', SalvarPedido.as_view(), name='salvarpedido'),
]
