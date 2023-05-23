from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=5, inventory=100)
        self.assertEqual(item.title, 'IceCream')
        self.assertEqual(item.price, 5)