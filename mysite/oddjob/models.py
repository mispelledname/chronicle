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
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    originUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='originUser')
    contributors = models.ManyToManyField(User, related_name='contributors')
    datePosted = models.DateTimeField()
    dateDue = models.DateTimeField()
    numHelperRequested = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    taskDuration = models.DurationField()
    def __str__(self):
        return self.title