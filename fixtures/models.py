from django.db import models
from django.contrib.postgres.fields import ArrayField
from club.models import Club

# Create your models here.


class Match(models.Model):
    host = models.ForeignKey(Club, null=True, related_name='home')
    guest = models.ForeignKey(Club, null=True, related_name='away')
    match_start_time = models.DateTimeField(db_index=True, null=True, blank=True)
    host_score = models.IntegerField(null=True, blank=True)
    guest_score = models.IntegerField(null=True, blank=True)
    goal_scorers = models.TextField(blank=True)
    status = models.CharField(max_length=32, blank=True)
