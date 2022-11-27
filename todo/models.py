from django.db import models

class todo(models.Model):
    title = models.CharField(max_length=500, null=True)
    memo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
