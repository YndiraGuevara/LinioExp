from django.contrib import admin
from .models import  *

# Register your models here.
admin.site.register(Localizacion)

admin.site.register(Categoria)
admin.site.register(Comerciante)
admin.site.register(ProductoImage)
admin.site.register(Pedido)
admin.site.register(DetallePedido)

# Importar clases Cliente y Colaborador
from .models import Cliente, Colaborador, Profile

class ClienteInline(admin.TabularInline):
    model=Cliente

class ColaboradorInline(admin.TabularInline):
    model=Colaborador

class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        ClienteInline,
        ColaboradorInline
    ]

admin.site.register(Cliente)
admin.site.register(Colaborador)
admin.site.register(Profile, ProfileAdmin)

class ProductoImageInline(admin.TabularInline):
    model=ProductoImage


class ProductoAdmin(admin.ModelAdmin):
    inlines = [
        ProductoImageInline,
    ]
admin.site.register(Producto, ProductoAdmin)