from django.db import models
from django.utils.timezone import now


class Sms(models.Model):
    sender = models.IntegerField()
    receptor = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"from {self.sender} sent to {self.receptor} ,context: {self.text}"