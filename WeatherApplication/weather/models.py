from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):  #show the actual city name on the dashboard
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        return super(City, self).save(*args, **kwargs)

    class Meta: #show the plural of city as cities insted of citys
        verbose_name_plural = 'cities'
