from django.db import models


class Finding(models.Model):
    target_id = models.CharField(max_length=60, unique=True)
    definition_id = models.CharField(max_length=60, unique=True)
    scans = models.CharField(max_length=60, unique=True)
    url = models.URLField(max_length=300)
    path = models.CharField(max_length=300)
    method = models.CharField(max_length=60)


# ● target_id
# ● definition_id
# ● scans
# ● url
# ● path
# ● method