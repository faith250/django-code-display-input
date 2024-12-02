from django.urls import path, include
from .views import ProductInfoViewSet
from rest_framework.routers import DefaultRouter
from .views import get_filtered_data

router = DefaultRouter()
router.register(r'products', ProductInfoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Make sure you include the router's URLs here
    path('api/filter/', get_filtered_data, name='get_filtered_data'),

]
