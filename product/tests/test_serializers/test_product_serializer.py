from django.test import TestCase

from product.models import Category, Product
from product.serializers.product_serializer import ProductSerializer


class ProductSerializerTest(TestCase):

    def test_product_serializer(self):
        category = Category.objects.create(title="Tecnologia", slug="tecnologia", active=True)

        product = Product.objects.create(title="Notebook", description="Notebook Dell", price=3000, active=True)

        product.categories.add(category)

        serializer = ProductSerializer(product)

        self.assertEqual(serializer.data["title"], "Notebook")
        self.assertEqual(serializer.data["description"], "Notebook Dell")
        self.assertEqual(serializer.data["price"], 3000)
        self.assertEqual(serializer.data["active"], True)
