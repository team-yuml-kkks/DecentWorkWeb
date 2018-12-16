from rest_framework import authentication, mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from decentwork.apps.engagments.models import Engagment
from decentwork.apps.engagments.serializers import EngagmentSerializer


class EngagmentsPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 1000


class EngagmentsViewSet(viewsets.ModelViewSet):
    """ViewSet for `Engagment` model."""

    queryset = Engagment.objects.filter(is_done=False).order_by('created')
    serializer_class = EngagmentSerializer
    authentication_classes = [authentication.TokenAuthentication]
    pagination_class = EngagmentsPagination

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer: EngagmentSerializer):
        serializer.save(owner=self.request.user)


class UserEngagmentsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """List of engagments which user created."""

    serializer_class = EngagmentSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Selects engagments created by user."""
        user = self.request.user
        return Engagment.objects.filter(owner=user)
