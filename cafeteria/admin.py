from django.contrib import admin
from cafeteria.models import Produto, Pedidos, PedidoCliente

# Register your models here.
admin.site.register(Produto)
admin.site.register(Pedidos)
admin.site.register(PedidoCliente)

