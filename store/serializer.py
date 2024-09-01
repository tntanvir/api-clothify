from rest_framework import serializers

from .models import Product,Review,Category,Cart,CartItems,Order, OrderItem
from authore.serializer import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField()  
    user = UserSerializer(read_only=True)
    size = serializers.ListField(child=serializers.CharField())
    color = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Product
        fields = '__all__'

    def validate_category(self, value):
        try:
            category = Category.objects.get(name=value)
            return category
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category does not exist")

    def create(self, validated_data):
        category_name = validated_data.pop('category')
        category = Category.objects.get(name=category_name)
        validated_data['category'] = category
        return super().create(validated_data)


    

class ReviewSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = '__all__'



class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    subTotal =serializers.SerializerMethodField('product_price')
    class Meta:
        model = CartItems
        fields = ['id','cart','product','quantity','subTotal','color','size']

    def product_price(self, cartitem:CartItems):
        return cartitem.product.price*cartitem.quantity
    

class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    items=CartItemSerializer(many=True)
    total_main =serializers.SerializerMethodField('total')

    class Meta:
        model = Cart
        fields = ['id','user','items','total_main','ordered']

    def total(self,cart:Cart):
        items=cart.items.all()
        total = sum([item.product.price*item.quantity for item in items])
        return total
    
# order

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'size', 'color', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'ordered_at', 'total', 'items']
