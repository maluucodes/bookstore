from django.test import TestCase

from product.models import Category, Product
from product.serializers.category_serializer import CategorySerializer
from product.serializers.product_serializer import ProductSerializer


class CategorySerializerTest(TestCase):

    def test_category_serializer(self):
        category = Category.objects.create(
            title="Livros",
            slug="livros",
            description="Categoria de livros",
            active=True
        )

        serializer = CategorySerializer(category)

        self.assertEqual(serializer.data["title"], "Livros")
        self.assertEqual(serializer.data["slug"], "livros")
        self.assertEqual(serializer.data["description"], "Categoria de livros")
        self.assertEqual(serializer.data["active"], True)


class ProductSerializerTest(TestCase):

    def test_product_serializer(self):
        category = Category.objects.create(
            title="Tecnologia",
            slug="tecnologia",
            active=True
        )

        product = Product.objects.create(
            title="Notebook",
            description="Notebook Dell",
            price=3000,
            active=True
        )

        product.categories.add(category)

        serializer = ProductSerializer(product)

        self.assertEqual(serializer.data["title"], "Notebook")
        self.assertEqual(serializer.data["description"], "Notebook Dell")
        self.assertEqual(serializer.data["price"], 3000)
        self.assertEqual(serializer.data["active"], True)