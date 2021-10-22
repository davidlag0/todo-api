"""todoapi Serializers"""

from rest_framework import serializers


# pylint: disable=too-few-public-methods
class PingSerializer(serializers.HyperlinkedModelSerializer):
    """Ping Serializer"""

    class Meta:
        """Ping Serializer metadata"""
