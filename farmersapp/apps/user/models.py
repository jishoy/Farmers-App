from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.conf import settings

# Create your models here.


class User(AbstractUser):
    name = models.CharField(_('name'), max_length=30, blank=True)
    village = models.CharField(_('village'), max_length=30, blank=True)
    district = models.CharField(_('district'), max_length=30, blank=True)
    group_name = models.CharField(_('group name'), max_length=30, blank=True)
    location = models.CharField(_('location'), max_length=30, blank=True)
    phone = models.CharField(blank=True, max_length=20, unique=True)
    password = models.CharField(_('password'), max_length=100, blank=True)


# class ExpiringToken(Token):
#
#     class Meta(object):
#         proxy = True
#
#     def expired(self):
#
#         now = timezone.now()
#         return self.created < now - settings.EXPIRING_TOKEN_LIFESPAN
