"""todoapi Views"""

from django.db.models.query import EmptyQuerySet
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from todoapi.api.serializers import PingSerializer


class PingViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows to PING the API.
    """

    queryset = EmptyQuerySet  # type: ignore
    serializer_class = PingSerializer

    def retrieve(self, request, *args, **kwargs) -> Response:
        return Response({"pong": kwargs["pk"]})
