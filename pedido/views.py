# from django.shortcuts import render

from django.http import HttpResponse
from django.views import View


class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')


class SalvarPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('FecharPedido')


class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')
