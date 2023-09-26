from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
from django.conf import settings
from django.core.validators import FileExtensionValidator

from .validators import validate_file_extension

# Create your models here.


class Time(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class File(Time):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(
        blank=False,
        null=False,
        upload_to="documents/%Y/%m/%d",
        validators=[validate_file_extension],
    )
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)
