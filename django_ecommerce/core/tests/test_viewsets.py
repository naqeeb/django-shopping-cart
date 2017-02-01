from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
import simplejson

from core.models import Store, Order, OrderItem

User = get_user_model()

class OrderViewSetTestCase(TestCase):
    fixtures = ['store_setup.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=self.user)

    def get(self, url):
        return self.client.get(url, format='json')

    def test_order_list_all(self):
        url = '/orders'
        expected_response = [{
                "external_id": "258836",
                "status": "New",
                "items": [{
                    "product": "A3",
                    "quantity": 2,
                    "price": "121.77"
                    }]
            },{
                "external_id": "305742",
                "status": "New",
                "items": [{
                    "product": "A3",
                    "quantity": 3,
                    "price": "121.77"
                    }]
            },{
                "external_id": "192157",
                "status": "New",
                "items": [{
                    "product": "A1",
                    "quantity": 1,
                    "price": "299.99"
                }, {
                    "product": "A2",
                    "quantity": 1,
                    "price": "99.99"
            }]
        }]

        response = self.get(url)
        actual_response = simplejson.loads(response.content)
        self.assertItemsEqual(actual_response, expected_response)

    def test_order_retrieval_by_id(self):
        url = '/orders/3'
        expected_response = {
                "external_id": "192157",
                "status": "New",
                "total": "399.98",
                "items": [{
                    "product": "A1",
                    "quantity": 1,
                    "price": "299.99"
                }, {
                    "product": "A2",
                    "quantity": 1,
                    "price": "99.99"
            }]
        }

        response = self.get(url)
        actual_response = simplejson.loads(response.content)
        self.assertDictEqual(actual_response, expected_response)

