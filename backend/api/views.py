from os import getenv

from django.db.models import Sum
from django.shortcuts import get_object_or_404

import stripe
from dotenv import load_dotenv
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .models import Item, Order
from .utils import get_order

load_dotenv()

stripe.api_key = getenv('STRIPE_API_KEY', default='default_stripe_api_key')
stripe_public_key = getenv('STRIPE_PUBLIC_KEY', default='default_pub_key')


class ItemListApi(APIView):
    '''
    Рендерит страницу со списком доступных итемов.
    '''
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        items = Item.objects.all()
        data = {
            'items': items,
        }
        return Response(data=data, template_name='items.html')


class ItemDetailApi(APIView):
    '''
    Рендерит страницу конкретного итема с возможность покупки или добавления
    в корзину. 
    '''
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        data = {
            'item_id': item_id,
            'name': item.name,
            'description': item.description,
            'price': item.price,
            'stripe_key': stripe_public_key
        }
        # запрос на текущую корзину, так как она не привязана к пользователю
        # или сессии и всегда будет в единичном экземпляре
        order = get_order()
        if order:
            total_cost = order.items.all().aggregate(Sum('price'))
            print(total_cost)
            order_data = {
                'cart_count_items': order.items.count(),
                'cart_total_cost': total_cost.get('price__sum'),
            }
            data.update(order_data)
        return Response(data=data, template_name='item.html')


class BuyDetailApi(APIView):
    '''
    Создает Stripe сессию на отдельный итем и возвращает
    json вида {'id': session.id}.
    '''
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        session = stripe.checkout.Session.create(
            success_url=request.build_absolute_uri('/items/'),
            cancel_url=request.build_absolute_uri(f'/item/{item_id}/'),
            mode='payment',
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                        },
                        'unit_amount': item.price,
                    },
                    'quantity': 1,
                },
            ],
        )
        return Response(data={'id': session.get('id')})


class AddToCartApi(APIView):
    '''
    Добавляет уникальный товар в корзину.
    '''
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        order = get_order()
        if not order:
            order = Order.objects.create()
        order.items.add(item)
        return Response(status=HTTP_200_OK)


class ClearCartApi(APIView):
    '''
    Очищает корзину.
    '''
    def get(self, requst):
        Order.objects.all().delete()
        return Response(status=HTTP_200_OK)


class BuyCartApi(APIView):
    '''
    Создает Stripe сессию на всю корзину с уникальными итемами и возвращает
    json вида {'id': session.id}.
    '''
    def get(self, request):
        order = get_order()
        line_items = []
        for item in order.items.all():
            item_data = {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }
            line_items.append(item_data)

        session = stripe.checkout.Session.create(
            success_url=request.build_absolute_uri('/items/'),
            cancel_url=request.build_absolute_uri('/items/'),
            mode='payment',
            line_items=line_items
        )
        return Response(data={'id': session.get('id')})
