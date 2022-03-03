import re
from django.test import RequestFactory, TestCase
from django.urls import reverse
from animais.views import index 

class AnimaisURLSTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_route_uses_index_view(self):
        request = self.factory.get('/')
        with self.assertTemplateUsed('index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)

