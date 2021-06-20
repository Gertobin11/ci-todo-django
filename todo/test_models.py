from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    def test_created_item_defults_to_not_done(self):
        item = Item.objects.create(name="test object")
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name="test item")
        self.assertEqual(str(item), "test item")
