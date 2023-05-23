from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title='IceCream', price=5, inventory=100)
        Menu.objects.create(title='Cake', price=10, inventory=50)

    def test_getall(self):
        self.setup()
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)