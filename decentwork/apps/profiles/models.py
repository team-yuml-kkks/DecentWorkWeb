from django.contrib.postgres.fields import ArrayField
from django.db import models

from decentwork.apps.cities.models import City
from decentwork.apps.common.models import User
from decentwork.apps.professions.models import Profession


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    phone_numbers = ArrayField(models.CharField(max_length=11, blank=True, null=True))
