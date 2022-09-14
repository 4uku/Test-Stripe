import json

from django.core.management.base import BaseCommand

from api.models import Item


class Command(BaseCommand):
    help = 'Загружает товары в базу'

    def add_objects(self, model: Item, reader):
        [model.objects.create(**row) for row in reader]
        return f'Database Update {model}'

    def handle(self, *args, **options):
        with open('items_data.json', 'rb') as f:
            items = json.load(f)
        self.stdout.write(
            self.style.SUCCESS(
                self.add_objects(Item, items)
            )
        )
