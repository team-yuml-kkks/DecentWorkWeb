from rest_framework import authentication, generics, mixins, viewsets
from rest_framework.exceptions import ParseError
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from decentwork.apps.engagments.models import Engagment, UserAssigned
from decentwork.apps.engagments.serializers import (EngagmentSerializer,
                                                    AssignEngagmentSerializer)


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
        actions = ['create', 'update', 'partial_update']
        if self.action in actions:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer: EngagmentSerializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer: EngagmentSerializer):
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


class AssignUserViewSet(mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """Create assign between user and engagment or delete it."""
    serializer_class = AssignEngagmentSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'engagment_id'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Selects user's assigned engagments to perform delete."""
        user = self.request.user
        return UserAssigned.objects.filter(user=user)


class ListAssigment(generics.ListAPIView):
    serializer_class = AssignEngagmentSerializer
    authentication_classes = []

    def get_queryset(self):
        engagment = self.request.query_params.get('engagment', None)

        if engagment is None:
            raise ParseError('No engagment passed')

        return UserAssigned.objects.filter(engagment=engagment)
