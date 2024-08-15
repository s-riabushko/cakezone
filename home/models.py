from django.db import models


# Create your models here.
#
class CommonOption(models.Model):
    """
    model for common and special single entries: text or photo.
    """
    key = models.CharField(max_length=50, unique=True)
    value = models.TextField(max_length=1024, blank=True)
    photo = models.ImageField(upload_to='common_options_photos', blank=True)

    def __str__(self):
        return self.key


class Counter(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
    fa_link = models.CharField(max_length=64)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='testimonial_photos', blank=True)
    profession = models.CharField(max_length=50)
    testimonial_text = models.TextField()
    testimonial_date = models.DateField()
    sort = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'
