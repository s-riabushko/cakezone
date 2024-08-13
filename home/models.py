from django.db import models


# Create your models here.
#
class CommonOption(models.Model):
    """
    model for common and special single entries: text or photo.
    """
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=250, blank=True)
    photo = models.ImageField(upload_to='common_options_photos', blank=True)

    def __str__(self):
        return self.key


class Counter(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
    fa_link = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    testimonial_text = models.TextField()
    testimonial_date = models.DateField()
    sort = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
