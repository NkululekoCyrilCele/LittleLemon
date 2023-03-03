from datetime import datetime
from restaurant.models import Booking, MenuItem
from django.test import TestCase


class MenuItemTest(TestCase):
    def setUp(self):
        self.menu_item = MenuItem.objects.create(
            title='Burger', price=10.99, inventory=100)

    def test_menu_item_title(self):
        self.assertEqual(self.menu_item.title, 'Burger')

    def test_menu_item_price(self):
        self.assertEqual(self.menu_item.price, 10.99)

    def test_menu_item_inventory(self):
        self.assertEqual(self.menu_item.inventory, 100)


class BookingTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            name='John Doe', no_of_guests=4, booking_date=datetime.now())

    def test_booking_name(self):
        self.assertEqual(self.booking.name, 'John Doe')

    def test_booking_no_of_guests(self):
        self.assertEqual(self.booking.no_of_guests, 4)

    def test_booking_booking_date(self):
        self.assertIsInstance(self.booking.booking_date, datetime)

    def test_booking_str(self):
        self.assertEqual(str(self.booking), 'John Doe')
