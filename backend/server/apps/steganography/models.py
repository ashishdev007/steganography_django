from djongo import models

# Create your models here.


class StatusTracker(models.Model):
    _id = models.ObjectIdField()
    created = models.DateTimeField(auto_now=True)
    progress = models.IntegerField(default=0)