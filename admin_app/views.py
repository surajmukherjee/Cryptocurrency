from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
# from django.db.models import Q
# from admin_app.forms import
# from admin_app.models import RoleDetail
# from Functions.


def indexPage(request):
    return render(request, 'index.html')


def signUpPage(request):
    return render(request, 'signup.html')


def loginPage(request):
    return render(request, 'login.html')


