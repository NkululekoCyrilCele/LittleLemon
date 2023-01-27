from django.test import TestCase, RequestFactory
from restaurant.models import MenuItem
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuItemSerializer

mocks = [
    {
        'title': 'Apples',
        'price': 50,
        'inventory': 1,
    },
    {
        'title': 'Oranges',
        'price': 60,
        'inventory': 2,
    },
    {
        'title': 'Banana',
        'price': 40,
        'inventory': 3,
    },
]


class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        for mock in mocks:
            MenuItem.objects.create(
                title=mock.title,
                price=mock.price,
                inventory=mock.inventory
            )

    def test_getall(self):
        menuitems = MenuItem.objects.all()
        serialized_menuitems = MenuItemSerializer(menuitems, many=True)
        request = self.factory.get('restaurant/menu/')
        response = MenuItemsView.as_view()(request)

        self.assertEqual(response.data, serialized_menuitems.data)
