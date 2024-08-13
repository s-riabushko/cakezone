from django.db import models


# Create your models here.
class MasterChefs(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='staff_photos')
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField()
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name
