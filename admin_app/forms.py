from __future__ import unicode_literals
from django import forms
from admin_app.models import RoleDetail


class SignUpForm(forms.ModelForm):
    class Meta:
        model = RoleDetail
        exclude = ["name", "email", "password", "address", "gender", "mobile", "otp", "otp_time", "verify_link",
                   "is_active", "role"]
