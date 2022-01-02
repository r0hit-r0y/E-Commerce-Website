#from django.test import TestCase
import unittest
from views import home_view
from migrations import views

class MigrationsViewsTestCase(unittest.TestCase):
    def test_home_view(self):
        home_view = views.home_view('ecom/index.html')
        self.assertEqual(home_view,'ecom/index.html')

if __name__ == '_main_':
    unittest.main()
# Create your tests here.
