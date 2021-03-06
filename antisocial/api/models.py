from django.db import models
from django.contrib.auth.models import AbstractUser, User as AuthUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class NeighborHood(models.Model):
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    admin = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE, related_name='user')
    date_created = models.DateTimeField(_('date created'), default=timezone.now)
    created_by = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE, related_name='created_by')


class User(AbstractUser):
    email = models.EmailField(_('email'), unique=True)
    neighborhood = models.ForeignKey(NeighborHood, blank=True, null=True, on_delete=models.CASCADE)


class Business(models.Model):
    name = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE)
    email = models.EmailField(_('email'))
    date_created = models.DateTimeField(_('date created'), default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_created_by')


class Post(models.Model):
    content = models.TextField()
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(_('date created'), default=timezone.now)


class ContactInfo(models.Model):
    facility = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=12)
    Phone_number_2 = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(_('email'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE)
    date_created = models.DateTimeField(_('date created'), default=timezone.now)
