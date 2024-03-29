from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from cafeteria.models import Produto
from cafeteria.models import PedidoCliente, Pedidos
from serial import Serial

SERIAL_PORT = "COM4"

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
    disco = dict(request.GET)

    l = len(nome['nome'])
    new_nome = []
    new_quantidade = []
    new_valor = []
    new_total_parcial = []
    new_cliente = ''
    new_disco = ''

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

def pedido_salvo(request):

    nome = dict(request.GET)
    quantidade = dict(request.GET)
    valor = dict(request.GET)
    total = dict(request.GET)

    cliente = dict(request.GET)
    disco = dict(request.GET)
    total_geral = dict(request.GET)


    pedido_str = ""
    itens_str = ""

    l = len(nome['nome'])

    new_nome = []
    new_quantidade = []
    new_valor = []
    new_total = []

    new_cliente = []
    new_disco = []
    new_total_geral = []

    new_cliente.append(cliente['cliente'][0])
    new_disco.append(disco['disco'][0])
    new_total_geral.append(total_geral['total_geral'][0])

    try:
        tem_porta = True
        try:
            ser = Serial(SERIAL_PORT, 19200, timeout=1)
        except:
            print('Erro de comunicação com porta serial.')
            tem_porta = False
        for i in range(l):
            new_nome.append(nome['nome'][i])
            new_quantidade.append(quantidade['quantidade'][i])
            new_valor.append(valor['valor'][i])
            new_total.append(total['total'][i])

    

        cliente_pedido = PedidoCliente()

        cliente_pedido.nome_cliente = new_cliente[0]
        cliente_pedido.disco_pedido = new_disco[0]
        cliente_pedido.total_geral = float(new_total_geral[0])
        cliente_pedido.finalizado = False
        cliente_pedido.save()
        pedido_str = str.encode(f"Cliente: {new_cliente[0]}\nNumero Disco: {new_disco[0]}\n")
        if tem_porta == True:
            ser.write(pedido_str)

        for i in range(l):
        
            pedidos = Pedidos()
            pedidos.nome = new_nome[i]
            pedidos.quantidade = new_quantidade[i]
            pedidos.valor = new_valor[i]
            pedidos.total = new_total[i]
            pedidos.pedido_cliente = cliente_pedido
            pedidos.save()

            itens_str = str.encode(f"Item: {new_nome[i]}\nQuantidade: {new_quantidade[i]}\n")
            if tem_porta == True:
                ser.write(itens_str)
        if tem_porta == True:
            ser.write(b"#######################\n\n")
            ser.close()
    except:
        print('Não foi possível salvar dados.')
    context = {
        'cliente': new_cliente[0],
        'disco': new_disco[0],
        'total': new_total_geral[0],
    }  
    return render(request, 'cafeteria/pedido_salvo.html', context=context)

def painel(request):

    # pedido_clientes = PedidoCliente.objects.all()
    pedidos = Pedidos.objects.all()

    # for p in pedido_clientes:


    id_old = -1
    cliente = []

    if len(pedidos) > 0:

        for p in pedidos:

            if p.pedido_cliente_id != id_old:
                cliente.append(PedidoCliente.objects.get(id=p.pedido_cliente_id))
                # print(f'CLIENTE: {cliente}')
            
            id_old = p.pedido_cliente_id

        context = { 
            'pedido_cliente': cliente,
            'pedidos': pedidos
        }
        return render(request, 'cafeteria/painel_pedidos.html', context=context)
    else:
        return redirect('home')



def finalizar_pedido(request):

    deletar = dict(request.GET)
    valor = []

    cliente = PedidoCliente.objects.all()
    for c in deletar.keys():
        # print(deletar[c][0])
        valor.append(deletar[c][0])

    # print(deletar.keys())

    try:
    
        id_delete = zip( cliente, valor )
        for d, c in id_delete:
            print(type(c))
            try:
                if c == 'true':
                    pedido = Pedidos.objects.filter(pedido_cliente_id=int(d.id))

                    cliente = PedidoCliente.objects.filter(id=int(d.id))

                    pedido.delete()
                    cliente.delete()
            except:
                print('Registro não existe...')
    except:
        print("Não foi selecionado nenhum item.")
        

    
    
    return redirect('painel')
