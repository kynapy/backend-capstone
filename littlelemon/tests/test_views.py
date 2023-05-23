from django.test import TestCase
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='IceCream', price=5, inventory=100)
        Menu.objects.create(title='Cake', price=10, inventory=50)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data, serializer.data)