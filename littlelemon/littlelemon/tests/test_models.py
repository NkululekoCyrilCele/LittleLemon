from django.test import TestCase
from restaurant.models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(
            title='Apples',
            price=50.00,
            inventory=1
        )
        self.assertEqual(item, 'Apples : 50')
