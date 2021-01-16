from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.conf import settings

import datetime

# Create your models here.


class User(AbstractUser):
    name = models.CharField(_('name'), max_length=30, blank=True)
    village = models.CharField(_('village'), max_length=30, blank=True)
    district = models.CharField(_('district'), max_length=30, blank=True)
    group_name = models.CharField(_('group name'), max_length=30, blank=True)
    location = models.CharField(_('location'), max_length=30, blank=True)
    phone = models.CharField(blank=True, max_length=20, unique=True)
    password = models.CharField(_('password'), max_length=100, blank=True)
    profile_images = models.ImageField(upload_to ='uploads/profile-images')

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.username

    def save(self, *args, **kwargs):
        if self.username == "":
            self.username = self.phone
        super(User, self).save(*args, **kwargs)


# this model Stores the data of the Phones Verified
class UserOtp(models.Model):
    phone = models.BigIntegerField(blank=False, unique=True)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)   # For HOTP Verification

    def __str__(self):
        return str(self.phone)


class Transaction(models.Model):
    TRANSACTION_CHOICES = (
        ('credit', 'CREDIT'),
        ('debit', 'DEBIT'),
    )
    user = models.ForeignKey(User, related_name='user_transaction', on_delete=models.CASCADE)
    date_of_transaction = models.DateField(_("Date"), default=datetime.date.today)
    amount = models.BigIntegerField()
    status = models.CharField(max_length=6, choices=TRANSACTION_CHOICES, default='credit')
    purpose = models.TextField()

    def __str__(self):
        return str(self.user)


class ExpiringToken(Token):

    class Meta(object):
        proxy = True

    def expired(self):
        now = timezone.now()
        return self.created < now - settings.EXPIRING_TOKEN_LIFESPAN
