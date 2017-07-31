from django.db import models

class Bucketlist(models.Model):
    name = models.CharField(blank=False, max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "{}".format(self.name)
