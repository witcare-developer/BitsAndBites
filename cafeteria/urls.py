from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/<int:produto_id>', views.detalhe_produto, name='produtos'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedido_salvo/', views.pedido_salvo, name='pedido_salvo'),
    path('painel/', views.painel, name='painel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)