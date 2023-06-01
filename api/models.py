from django.db import models

# Create your models here.


class Job(models.Model):

    title = models.CharField(max_length=255, unique=True)
    brief_details = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=255, unique=True)
    application_email = models.EmailField(max_length=100, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    job_image = models.ImageField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=300)
    required_connect = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title


class JobStack(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,)

    def __str__(self) -> str:
        return self.name
