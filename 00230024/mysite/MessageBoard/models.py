from django.db import models


# Create your models here.
class Commenter(models.Model):
    commenter_name = models.CharField(max_length=100)
    commenter_time = models.DateTimeField('Time to leave a message')
    commenter_content = models.CharField(max_length=400)

    def __str__(self):
        return self.commenter_name + self.commenter_content
