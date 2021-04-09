from django.db import models

# Create your models here.




class User(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __str__(self):
        return self.tag

class Job(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    originUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='originUser', null=True, blank=True)
    contributors = models.ManyToManyField(User, related_name='contributors', null=True, blank=True)
    datePosted = models.DateTimeField(null=True, blank=True)
    dateDue = models.DateTimeField(null=True, blank=True)
    numHelperRequested = models.IntegerField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    taskDuration = models.DurationField(null=True, blank=True)
    def __str__(self):
        return self.title