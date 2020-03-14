from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from admin_app.forms import SignUpForm
from admin_app.models import RoleDetail
from Functions.generateString import generateString
from Functions.verifyMail import verify_mail_send


def indexPage(request):
    return render(request, 'index.html')


def signUpPage(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            sg = signup_form.save(commit=False)
            sg.name = request.POST["fullname"]
            sg.email = request.POST["email"]
            sg.password = make_password(request.POST["Password"])
            sg.gender = request.POST["gender"]
            sg.mobile = request.POST["mobile"]
            # sg.role_id = request.POST["role"]
            string = make_password(generateString()).replace("+", "")
            full_link = r"127.0.0.1:8000/verify/?token={}".format(string)
            sg.verify_link = string
            sg.save()
            verify_mail_send(request.POST['email'], request.POST['fullname'], full_link)
            return HttpResponse("<h1> Sign Up Process Complete, Check your Mail Id for verification link</h1>")
        else:
            return HttpResponse("<h1>Page Not Found</h1>")
    return render(request, 'signup.html')


def linkVerify(request):
    try:
        token = request.GET['token']
    except Exception as error:
        return HttpResponse(error)
    else:
        if RoleDetail.objects.filter(verify_link=token).exists():
            update = RoleDetail(email=RoleDetail.objects.get(verify_link=token).email, verify_link="", is_active=1)
            update.save(update_fields=['verify_link', 'is_active'])
            return redirect("/logInPage/")
        else:
            return HttpResponse("<h1>Invalid Response</h1>")


def loginPage(request):
    if request.method == 'POST':
        if RoleDetail.objects.filter(email=request.POST['email'].exists()) is True:
            user_data_email = RoleDetail.objects.get(email=request.POST['email'])
            if check_password(request.POST['Password'], user_data_email.password):
                print("User Found")
                if user_data_email.is_active == 1:
                    # print("User Is Active and Verified")
                    return HttpResponse("<h1>User Is ACTIVE </h1>")
                else:
                    if user_data_email.verify_link != "":
                        return render(request, 'login.html', {'verify_mail_notDone ': True})
                    else:
                        return render(request, 'login.html', {'permission_denied': True})
            else:
                return render(request, 'login.html', {'invalid_password': True})
        else:
            return render(request, 'login.html', {'invalid_email': True})
    return render(request, 'login.html')


