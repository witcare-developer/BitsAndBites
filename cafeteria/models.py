from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.TextField(null=False, blank=False, default='')
    descricao = models.TextField(null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)
    imagem = models.ImageField(upload_to='cafeteria/img', default='', null=False, blank=False)

    def __str__(self):
        return self.nome
class PedidoCliente(models.Model):
    nome_cliente = models.TextField(null=False, blank=False)
    disco_pedido = models.IntegerField(null=False, blank=False)
    total_geral = models.FloatField(null=False, blank=False)
    finalizado = models.BooleanField(default=False)
    
    def __str__(self) :
        return self.nome_cliente
class Pedidos(models.Model):
    pedido_cliente =  models.ForeignKey(PedidoCliente, on_delete=models.CASCADE)
    nome = models.TextField(null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    total = models.FloatField(null=False, blank=False)

    def __str__(self) :
        return self.nome
    