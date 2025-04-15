from django.db import models

class Website(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    layout = models.JSONField()  # JSONField for storing website structure
