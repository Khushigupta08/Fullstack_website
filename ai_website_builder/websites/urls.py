from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import WebsiteViewSet
from .views import generate_view,manage_view,delete_view,edit_view,preview_view

app_name = 'websites'

# Create a router and register our WebsiteViewSet with it.
router = DefaultRouter()
router.register(r'websites', WebsiteViewSet, basename='website')

urlpatterns = [
    path('generate/', generate_view, name='generate'),
    path('manage/', manage_view, name='manage'),
    # Include the router's URLs
    path('api/', include(router.urls)),
    path('delete/<int:website_id>/', delete_view, name='delete'),
    path('edit/<int:website_id>/', edit_view, name='edit'),
    path('preview/<int:pk>/', preview_view, name='preview'),
]
