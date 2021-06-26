from django.shortcuts import render
from .models import User
from django.contrib.auth.hashers import make_password, check_password
import random
import qrcode

login_otp = 0


# Create your views here.
def login(request):
    return render(request, "login.html")


def validate_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    hashedPassword = make_password(password=password)
    user = User(email=email, password=hashedPassword)
    user.save()
    user = User.objects.get(email=email)
    flag = check_password(password=password, encoded=user.password)
    print(flag)
    if flag:
        rno = random.randint(100000, 999999)
        global login_otp
        login_otp = rno
        im = qrcode.make("OTP: " + str(rno))
        im.save(r"qrapp/static/qrapp/qrimage/qrimage.jpg")
        return render(request, "qrcode_page.html")
    else:
        return render(request, 'login.html', {'error': 'Email or Password Invalid'})


def validate_otp(request):
    user_otp = request.POST.get('login_otp')
    if user_otp == str(login_otp):
        return render(request, "welcomw.html")
    else:
        return render(request, 'login.html', {"message": "Invalid otp"})
