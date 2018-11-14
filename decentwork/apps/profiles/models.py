from django.contrib.postgres.fields import ArrayField
from django.db import models

from decentwork.apps.cities.models import City
from decentwork.apps.common.models import User
from decentwork.apps.professions.models import Profession


class UserProfile(models.Model):
    """User's profile for more information about user.

    Attributes:
        user (User): One to one foreign key connected with User model.
        city (City): Foreign key to City model.
        professions (Profession): Foreign keys to profession model.
        description (str): User's information about himself.
        phone_numbers (ArrayField(str)): User's phone numbers.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    professions = models.ManyToManyField(Profession, blank=True)

    description = models.TextField(blank=True, null=True)
    phone_numbers = ArrayField(models.CharField(max_length=11, blank=True, null=True), blank=True, null=True)

    def __str__(self):
        return self.user.email
