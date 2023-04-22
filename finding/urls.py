from django.urls import path

from finding.views import FindingListView

app_name = "finding"

urlpatterns = [
    path("finding/", FindingListView.as_view(), name="finding"),
]
