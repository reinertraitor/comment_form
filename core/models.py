from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    
    def __str__(self):
        return self.full_name

    def clean(self):
        if not len(self.phone) > 10:
            raise ValidationError(
                {'title': "Title should have at least 10 letters"})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
