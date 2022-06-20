from django.db import models

# Create your models here.
class Profile(models.Model):
    external_id = models.TextField(
        verbose_name='User id',
    ) 
    name = models.TextField(
        verbose_name='User name',
    )

    def __str__(self):
        return f"#{self.external_id} {self.name}"

    class Meta:
        verbose_name = 'Profile'