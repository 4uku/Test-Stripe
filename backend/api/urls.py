from django.urls import path

from .views import (AddToCartApi, BuyCartApi, BuyDetailApi, ClearCartApi,
                    ItemDetailApi, ItemListApi)

urlpatterns = [
    path('items/', ItemListApi.as_view(), name='items_list'),
    path('item/<int:item_id>/', ItemDetailApi.as_view(), name='item_detail'),
    path('buy/<int:item_id>/', BuyDetailApi.as_view(), name='buy_detail'),
    path(
        'add_to_cart/<int:item_id>/', AddToCartApi.as_view(),
        name='add_to_cart'),
    path('clear_cart/', ClearCartApi.as_view(), name='clear_cart'),
    path('buy_cart/', BuyCartApi.as_view(), name='buy_cart'),
]
