from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg

from decentwork.apps.cities.models import City
from decentwork.apps.common.models import User
from decentwork.apps.professions.models import Profession

class IntegerRangeField(models.IntegerField):

    def __init__(self, verbose_name=None , name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


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
    rating = fields.IntegerRangeField(min_value=0, max_value=5)

    def __str__(self):
        return self.user.email
    
    def calculate_avg(self):
        return UserProfile.objects.aggregate(Avg('rating'))
        


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
