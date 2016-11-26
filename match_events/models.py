from django.db import models
from club.models import Club
from fixtures.models import Match

# Create your models here.


class Goal(models.Model):
    scorername = models.CharField(max_length=160, null=True)
    scorerclub = models.ForeignKey(Club, null=True, related_name="forclub")
    scored_against = models.ForeignKey(Club, null=True, related_name="against")
    minute = models.IntegerField(null=True)
    type = models.CharField(max_length=32, null=True)  # penalty, header, autogol etc
    match = models.ForeignKey(Match, null=True, related_name="match")
