from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from restaurant.serializers import MenuItemSerializer
from restaurant.models import MenuItem, Booking
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

    def test_get_menu_items(self):
        response = self.client.get(self.menu_list_create_url)
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

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
        response = self.client.post(self.menu_list_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)
        self.assertEqual(response.data['title']
                         [0], 'This field may not be blank.')


class BookingModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.booking = Booking.objects.create(
            name='Test Booking',
            no_of_guests=2,
            booking_date='2023-03-03 12:00:00+02:00',
            user=self.user
        )

    def test_booking_str(self):
        self.assertEqual(str(self.booking), self.booking.name)

    def test_booking_user(self):
        self.assertEqual(self.booking.user, self.user)

    def test_booking_no_of_guests(self):
        self.assertEqual(self.booking.no_of_guests, 2)

    def test_booking_name(self):
        self.assertEqual(self.booking.name, 'Test Booking')

    def test_booking_booking_date(self):
        self.assertEqual(
            str(self.booking.booking_date),
            '2023-03-03 12:00:00+02:00'
        )
