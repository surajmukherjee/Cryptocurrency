from __future__ import unicode_literals
from django.contrib import admin
from admin_app.models import UserRole, CoinSymbol

# ADMIN PAGE USING UserRole MODEL DATABASE

admin.site.register(UserRole)
admin.site.register(CoinSymbol)

