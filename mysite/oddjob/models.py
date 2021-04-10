from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, null=True, blank=True)
    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __str__(self):
        return self.tag

class Job(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    originUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='originUser', null=True, blank=True)
    contributors = models.ManyToManyField(UserProfile, related_name='contributors', null=True, blank=True)
    datePosted = models.DateTimeField(null=True, blank=True)
    dateDue = models.DateTimeField(null=True, blank=True)
    numHelperRequested = models.IntegerField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    taskDuration = models.DurationField(null=True, blank=True)
    def __str__(self):
        return self.title