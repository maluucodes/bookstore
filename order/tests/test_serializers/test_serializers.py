from django.test import TestCase
from django.contrib.auth.models import User

from product.models import Category, Product
from order.models import Order
from order.serializers.order_serializer import OrderSerializer


class OrderSerializerTest(TestCase):

    def test_order_serializer(self):
        user = User.objects.create_user(
            username="maria",
            password="123456"
        )

        category = Category.objects.create(
            title="Livros",
            slug="livros",
            active=True
        )

        product = Product.objects.create(
            title="Livro Python",
            description="Livro sobre Python",
            price=100,
            active=True
        )

        product.categories.add(category)

        order = Order.objects.create(user=user)
        order.product.add(product)

        serializer = OrderSerializer(order)

        self.assertEqual(serializer.data["total"], 100)