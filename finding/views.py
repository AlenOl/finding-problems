from django.db.models import QuerySet
from rest_framework import generics
from finding.models import Finding
from finding.serializers import FindingSerializer


class FindingListView(generics.ListAPIView):
    serializer_class = FindingSerializer

    def get_queryset(self) -> QuerySet:
        queryset = Finding.objects.all()
        definition_id = self.request.query_params.get("definition_id")
        scans = self.request.query_params.get("scans")
        if definition_id and scans is not None:
            for scan in scans:
                queryset = queryset.filter(definition_id=definition_id).filter(scans__icontains=scan)
        return queryset
