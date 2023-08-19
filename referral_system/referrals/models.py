from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    referral_code = models.CharField(max_length=6, unique=True)
    invited_by = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    phone_number.verbose_name = _('Phone Number')
    referral_code.verbose_name = _('Referral Code')
    invited_by.verbose_name = _('Invited By')

    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True,
                                    related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission,verbose_name='user permissions',
                                              blank=True,related_name='custom_user_permissions')

