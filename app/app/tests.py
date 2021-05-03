from django.test import TestCase
from app.calc import add, sub

class calcTest(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(5,3),8)

    def test_sub_numbers(self):
        self.assertEqual(sub(5,3),2)