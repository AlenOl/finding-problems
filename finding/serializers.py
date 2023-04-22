from rest_framework import serializers

from finding.models import Finding


class FindingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finding
        fields = ("id", "target_id", "definition_id", "scans", "url", "path", "method")
