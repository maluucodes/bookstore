from django.test import TestCase

from product.models import Category
from product.serializers.category_serializer import CategorySerializer


class CategorySerializerTest(TestCase):

    def test_category_serializer(self):
        category = Category.objects.create(
            title="Livros",
            slug="livros",
            description="Categoria de livros",
            active=True,
        )

        serializer = CategorySerializer(category)

        self.assertEqual(serializer.data["title"], "Livros")
        self.assertEqual(serializer.data["slug"], "livros")
        self.assertEqual(serializer.data["description"], "Categoria de livros")
        self.assertEqual(serializer.data["active"], True)
