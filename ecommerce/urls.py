from rest_framework import routers

from .views import CartViewSet, OrderItemViewSet, ProductViewSet,CartItemViewSet,OrderViewSet

router = routers.DefaultRouter()

router.register(r'Product', ProductViewSet)
router.register(r'Cart', CartViewSet)
router.register(r'CartItem', CartItemViewSet)
router.register(r'Order', OrderViewSet)
router.register(r'OrderItem', OrderItemViewSet)



urlpatterns = router.urls