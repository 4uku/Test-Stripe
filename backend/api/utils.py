from .models import Order


def get_order():
    if Order.objects.exists():
        return Order.objects.first()
    return False
