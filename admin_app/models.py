from __future__ import unicode_literals
from django.db import models


# -*- CLASS FOR USER ROLE --> ADMIN, MANAGER, DEVELOPER -*-
class UserRole(models.Model):
    roleId = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=255, default="", blank=True, null=True, unique=True)

    # -*- Function for displaying roles in a proper way in the admin site and table -*-
    def __str__(self):
        return "{}.{}".format(self.roleId, str(self.roleName).upper())


# -*- CLASS FOR SIGNUP PAGE AS WELL AS LOG IN PAGE CREDENTIAL VERIFICATION
class RoleDetail(models.Model):
    # role = models.ForeignKey(UserRole, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, default="", null=True, unique=True)
    email = models.CharField(primary_key=True, max_length=255, default="")
    password = models.CharField(max_length=255, default="", null=True)
    address = models.TextField(max_length=255, default="", blank=True, null=True)
    gender = models.CharField(max_length=255, default="", blank=True, null=True)
    mobile = models.BigIntegerField(default="", blank=True, null=True)
    otp = models.CharField(max_length=255, default="", blank=True, null=True)
    otp_time = models.CharField(max_length=255, default="", blank=True, null=True)
    verify_link = models.CharField(max_length=255, default="", blank=True, null=True)
    is_active = models.NullBooleanField(default=0)
