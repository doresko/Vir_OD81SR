from django.db import models

class PNG(models.Model):
    title = models.CharField(max_length=64, blank=False, null=False)
    full_title = models.CharField(max_length=64, blank=False, null=False)
    description = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return(self.full_title)

class JPG(models.Model):
    title = models.CharField(max_length=64, blank=False, null=False)
    full_title = models.CharField(max_length=64, blank=False, null=False)
    description = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return(self.full_title)

class GIF(models.Model):
    title = models.CharField(max_length=64, blank=False, null=False)
    full_title = models.CharField(max_length=64, blank=False, null=False)
    description = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return(self.full_title)