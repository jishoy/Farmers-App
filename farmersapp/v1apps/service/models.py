from django.db import models
from v1apps.user.models import User
from django.utils.translation import ugettext_lazy as _


class Service(models.Model):
    SERVICE_CHOICES = (
        ('agronomist', 'Agronomist'),
        ('soil-test', 'Soil Test'),
        ('crop-advice', 'Crop Advice'),
        ('tech-fin-aid', 'Technical Financial Aid'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )
    user = models.ForeignKey(User, related_name='user_service', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    services = models.CharField(max_length=20, choices=SERVICE_CHOICES, default='agronomist')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date = models.DateField(_('Date'))
    remark = models.TextField(_('Remarks'), max_length=30, blank=True)

    def __str__(self):
        return str(self.user)
