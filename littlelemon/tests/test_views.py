from restaurant.serializers import MenuItemSerializer
from restaurant.models import MenuItem
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class MenuItemViewTestCase(APITestCase):
    def setUp(self):
        self.menu_item_1 = MenuItem.objects.create(
            title='Item 1', price=9.99, inventory=10)
        self.menu_item_2 = MenuItem.objects.create(
            title='Item 2', price=14.99, inventory=5)
        self.menu_list_create_url = reverse('menu_list_create')
        self.menu_detail_url = reverse(
            'menu_detail', kwargs={'pk': self.menu_item_1.pk})
        self.menu_create_url = reverse('menu_create')

    def test_get_menu_items(self):
        response = self.client.get(self.menu_list_create_url)
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_menu_item(self):
        data = {'title': 'New Item', 'price': 12.99, 'inventory': 3}
        response = self.client.post(self.menu_list_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MenuItem.objects.count(), 3)
        self.assertEqual(MenuItem.objects.get(id=3).title, 'New Item')

    def test_get_menu_item_detail(self):
        response = self.client.get(self.menu_detail_url)
        menu_item = MenuItem.objects.get(id=self.menu_item_1.pk)
        serializer = MenuItemSerializer(menu_item)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_menu_item(self):
        data = {'title': 'Updated Item', 'price': 19.99, 'inventory': 2}
        response = self.client.put(self.menu_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(MenuItem.objects.get(
            id=self.menu_item_1.pk).title, 'Updated Item')

    def test_delete_menu_item(self):
        response = self.client.delete(self.menu_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MenuItem.objects.count(), 1)

    def test_create_menu_item_with_invalid_data(self):
        data = {'title': '', 'price': 12.99, 'inventory': 3}
        response = self.client.post(self.menu_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)
        self.assertEqual(response.data['title']
                         [0], 'This field may not be blank.')
