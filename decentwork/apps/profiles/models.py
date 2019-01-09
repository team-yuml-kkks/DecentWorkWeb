from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg

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


class Rating(models.Model):
    rating = models.IntegerField(blank=True, null=True, validators=[
        MaxValueValidator(5), MinValueValidator(1)
    ])
    rated_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rated_user")
    rating_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rating_user")

    class Meta:
        unique_together = ('rated_user', 'rating_user')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
