from django.urls import include, path

from rest_framework import routers

from product.views import ProductViewSet


app_name = 'product'

router = routers.DefaultRouter()
router.register("products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls))
]
