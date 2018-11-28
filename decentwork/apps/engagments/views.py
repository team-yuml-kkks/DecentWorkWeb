from rest_framework import viewsets

from decentwork.apps.engagments.models import Engagment
from decentwork.apps.engagments.serializers import EngagmentSerializer


class EngagmentsViewSet(viewsets.ModelViewSet):
    """ViewSet for `Engagment` model."""

    queryset = Engagment.objects.all()
    serializer_class = EngagmentSerializer
    authentication_classes = []

    def perform_create(self, serializer: EngagmentSerializer):
        serializer.save(owner=self.request.user)
