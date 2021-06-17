from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('Inicio', views.Saludo, name='saludo'),
    path('productos', views.ProductListView.as_view(), name='product-list'),
    path('productos/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('Localizacion', views.LocalListView.as_view(), name='Local-list'),
    path('Localizacion/<int:pk>', views.LocalDetailView.as_view(), name='Local-detail'),
    path('add_to_cart/<int:product_pk>', views.AddToCartView.as_view(), name='add-to-cart'),
    path('remove_from_cart/<int:product_pk>', views.RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('carrito/', views.PedidoDetailView.as_view(), name='pedido-detail'),
    path('checkout/<int:pk>', views.PedidoUpdateView.as_view(), name='pedido-update'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('complete_payment/', views.CompletePaymentView.as_view(), name='complete-payment'),
    path('registro/', views.RegistrationView.as_view(), name='register'),
    #path("Nombre del url", view, name="para llamarlo luego")
]
