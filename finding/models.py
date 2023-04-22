from django.db import models


class Finding(models.Model):
    target_id = models.CharField(max_length=60, unique=True)
    definition_id = models.CharField(max_length=60, unique=True)
    scans = models.CharField(max_length=300, unique=True)
    url = models.URLField(max_length=300)
    path = models.CharField(max_length=300)
    method = models.CharField(max_length=60)

    def __str__(self):
        return f"target_id: {self.target_id}, definition_id: {self.definition_id}, " \
               f"scans: {self.scans}, url: {self.url}, path: {self.path}, method: {self.method}"
