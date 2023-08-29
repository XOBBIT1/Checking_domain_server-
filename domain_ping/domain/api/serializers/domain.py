from rest_framework import serializers

from ...models import Domain


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = [
            "domain_name",
        ]
        read_only = ["ping_of_domain"]


class DomainPingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = [
            "domain_name",
            "ping_of_domain",
        ]
