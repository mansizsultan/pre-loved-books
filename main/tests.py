from django.test import TestCase, Client
from django.utils import timezone
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/mogwartz/')
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self):
        result = Product.objects.create(
          name="MANSIZ",
          author = "MANSIZ",
          price = 69000,
          description = "I LOVE FASILKOM",
        )
        self.assertTrue(result.is_book_expensive)