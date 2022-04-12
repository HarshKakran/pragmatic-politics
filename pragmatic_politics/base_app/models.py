from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class LeaderInfo(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField(null=True, blank=True)

    criminal_records = ArrayField(
        models.CharField(max_length=512, null=True, blank=True)
    )
    promises_status = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    recent_news = ArrayField(
        models.URLField(null=True, blank=True)
    )


class PartyDetails(models.Model):
    name = models.CharField(max_length=200)
    ideology = models.TextField(null=True, blank=True)
    recent_news = ArrayField(models.URLField(null=True, blank=True))
    current_leaders = models.ManyToManyField(LeaderInfo)
