from django.db import models


class ForTest(models.Model):
    name = models.CharField(max_length="15", unique=True)
    processed = models.BooleanField(default=False)
