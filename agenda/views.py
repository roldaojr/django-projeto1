# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contato
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory


def index(request):
    return HttpResponse('Olá mundo')


def listar(request):
    contatos = Contato.objects.all()
    return render(request, 'agenda/contato_listar.html', {'itens': contatos})

ContatoForm = modelform_factory(Contato, fields=('__all__'))


def adicionar(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('contato_listar'))
    else:
        form = ContatoForm()
    return render(request, 'agenda/contato_form.html', {'form': form})
