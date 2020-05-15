from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Receita


# Create your views here.

def index(request):
    receitas = Receita.objects.order_by('-date_time').filter(publicada=True)
    paginator = Paginator(receitas, 1)  # Quantidade de receitas exibidas
    page = request.GET.get('page')
    receitas_pagina = paginator.get_page(page)
    dados = {'receitas': receitas_pagina}
    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {'receita': receita}
    return render(request, 'receita.html', receita_a_exibir)


def buscar(request):
    lista_receitas = Receita.objects.order_by('nome_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'buscar.html', dados)