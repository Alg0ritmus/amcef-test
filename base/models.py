from django.db import models


# Create your models here.

class  Post(models.Model):
    # id -> default by django (litesql) known as pk (PrimaryKey)
    userId = models.IntegerField()
    title = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)    

    def __str__(self) -> str:
        return ("userId: %d | title: %s" % (self.userId, self.title))