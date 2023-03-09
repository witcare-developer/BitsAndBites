from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from cafeteria.models import Produto

# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'cafeteria/home.html', context=context)

def detalhe_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    context = {
        'produto': produto
    }
    return render(request, 'cafeteria/produto.html', context=context)

def pedidos(request):

    nome = dict(request.GET)
    quantidade = dict(request.GET)
    valor = dict(request.GET)
    cliente = dict(request.GET)
    disco = dict(request.GET)

    l = len(nome['nome'])
    new_nome = []
    new_quantidade = []
    new_valor = []
    new_total_parcial = []
    new_cliente = ''
    new_disco = ''

    total_parcial = 0.0
    total_geral = 0.0

    for i in range(l):
        if int( quantidade['quantidade'][i] ) != 0:
            new_nome.append(nome['nome'][i])
            new_quantidade.append(quantidade['quantidade'][i])
            new_valor.append(valor['valor'][i])

    for i in range(len(new_nome)):
        new_total_parcial.append( float(new_valor[i]) * int(new_quantidade[i]))

    new_cliente = disco['cliente'][0]
    new_disco = disco['disco'][0]
    
    for total, qtd in zip(new_valor, new_quantidade):
        total_geral += ( float(total) * int(qtd) )

    value_zip = zip(new_nome, new_quantidade, new_valor, new_total_parcial)

    context = {
        'disco': new_disco,
        'cliente': new_cliente,
        'produtos': value_zip,
        'total': round(total_geral, 2)
    }

    return render(request, 'cafeteria/pedido.html', context=context )
    # return redirect('home')
