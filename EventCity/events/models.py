from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from users.models import Profile, Team

user = get_user_model()

Profile = Profile
Team = Team


class Category(models.Model): 
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
        

class PersonEvent(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=500, null=True, blank=True)

    creater = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='personEventCreater')
    
    users = models.ManyToManyField(Profile, blank=True, null=True)
    cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('PersonEventDetail', kwargs={'pk': self.pk})
    
    
class Event(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    city = models.CharField(max_length=455)
    address = models.CharField(max_length=255)
    
    creater = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='EventAdmin')
    
    users = models.ManyToManyField(Profile, blank=True, null=True)
    cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('EventDetail', kwargs={'pk': self.pk})
    

class TeamEvent(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=500, null=True, blank=True)

    creater = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='teamEventCreater')

    teams = models.ManyToManyField(Team, blank=True, null=True, related_name='TeamEventsTeams')
    cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('TeamEventDetail', kwargs={'pk': self.pk})

class TeamRequest(models.Model):
    from_profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='from_profile')
    to_profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='to_profile')
    is_checked = models.BooleanField(default=False)
        
