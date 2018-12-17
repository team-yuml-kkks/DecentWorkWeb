from django.db import models
from django.utils import timezone

from decentwork.apps.cities.models import City
from decentwork.apps.common.models import User
from decentwork.apps.professions.models import Profession


class Engagment(models.Model):
    """User's engagments model.

    Arguments:
        owner(`User`): User who creates engagment.
        profession(`Profession`): Profession for created engagment.
        city(`City`): City where engagment take place.
        title: Engagment title.
        description: Engagment description.
        created: Created time set as now().
        is_done: Determines if engagment is done or not.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(editable=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Adds to created as time now."""
        self.created = timezone.now()
        return super().save(*args, **kwargs)


class UserAssigned(models.Model):
    """Stores users which assign themselfs to single engagment.
    
    Attributes:
        engagment('Engagment'): Engagment which user assigned yourself.
        user('User'): Assigned user.
    """
    engagment = models.ForeignKey(Engagment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
