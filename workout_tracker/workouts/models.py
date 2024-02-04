from django.db import models

# Create your models here.
class Workout(models.Model):
    duration = models.DurationField()
    distance = models.FloatField()
    route_name = models.CharField(max_length = 100)
    heart_rate = models.IntegerField()
    date_time = models.DateTimeField()
    image = models.ImageField(upload_to = 'images/', blank = True, null = True)

    def __str__(self):
        return self.route_name
