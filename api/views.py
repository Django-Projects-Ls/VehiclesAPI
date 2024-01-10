from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Vehicle
from .serializers import VehicleSerializer


class VehicleViewSet(ModelViewSet):
    """API endpoint defined with ModelViewSet that allow us to do CRUD."""

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAdminUser]
