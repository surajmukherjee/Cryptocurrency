from __future__ import unicode_literals
from django import forms
from admin_app.models import RoleDetail, CoinSymbol


class SignUpForm(forms.ModelForm):
    class Meta:
        model = RoleDetail
        exclude = ["name", "email", "password", "address", "gender", "mobile", "otp", "otp_time", "verify_link",
                   "is_active", "role"]


class CoinListForm(forms.ModelForm):
    class Meta:
        model = CoinSymbol
        exclude = ["c_id", "c_name", "c_symbol"]
