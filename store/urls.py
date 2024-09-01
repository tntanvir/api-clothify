from django.urls import path
from .views import ProductDetailAPIView, ProductListCreateAPIView, ReviewListCreateAPIView, ReviewDetailAPIView, CategoryView, TopProductsAPIView,CartView,CheckoutAPIView,CustomerOrderHistoryAPIView, SellerOrderHistoryAPIView,CheckProductInOrderHistoryAPIView,ProductFilterByCategoryAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('category/', CategoryView.as_view(), name='category'),
    path('product/category/', ProductFilterByCategoryAPIView.as_view(), name='category'),

    path('products/<int:product_id>/reviews/', ReviewListCreateAPIView.as_view(), name='product-reviews'),
    path('reviews/<int:review_id>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('order-history/check-product/<int:product_id>/', CheckProductInOrderHistoryAPIView.as_view(), name='check-product-in-order-history'),
    path('products/top/', TopProductsAPIView.as_view(), name='top-products'),
    path('cart/', CartView.as_view(), name='cart'),  
    path('cart/item/<int:item_id>/', CartView.as_view(), name='cart-item'),  
    path('checkout/', CheckoutAPIView.as_view(), name='checkout'),
    path('orders/history/customer/', CustomerOrderHistoryAPIView.as_view(), name='customer-order-history'),
    path('seller-order-history/', SellerOrderHistoryAPIView.as_view(), name='seller-order-history'),
    
    
]