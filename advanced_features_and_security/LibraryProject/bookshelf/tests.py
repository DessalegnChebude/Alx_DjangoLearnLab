from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Book

class SecurityTests(TestCase):
    def test_sql_injection(self):
        # Attempt SQL injection through a search form
        response = self.client.get('/search/', {'query': "1 OR 1=1"})
        self.assertContains(response, "No results found")

