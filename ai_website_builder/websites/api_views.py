from rest_framework.viewsets import ModelViewSet
from .models import Website
from .serializers import WebsiteSerializer
from rest_framework.permissions import IsAuthenticated

class WebsiteViewSet(ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can access
