import base64
import json
import os.path
import subprocess

import requests
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import FormView

from .forms import CustomUserCreationForm, PasswordChangingForm
from .models import CustomUser


# class ExtendedEncoder(DjangoJSONEncoder):
#     def default(self, o):
#         if (isinstance(o, BufferedReader)) | (isinstance(o, ResizedImageFieldFile) | (isinstance(o, TextIOWrapper))):
#             return str(o)
#         else:
#             return super().default(o)


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = '/login'


def error(request):
    return render(request, 'main/404.html')


# @login_required
def main_page(request):
    if request.user.is_active:
        serials = subprocess.check_output('wmic diskdrive get SerialNumber').decode().split('\n')[1:]
        serials = [s.strip() for s in serials if s.strip()]
        # serials.pop()
        request.session['user_id'] = request.user.id
        image_file = f'media/{request.user.image}'
        with open(image_file, "rb") as f:
            im_bytes = f.read()
        im_b64 = base64.b64encode(im_bytes).decode("utf8")
        payload = json.dumps({"image1": im_b64, 'name_of_user': request.user.username, 'disk': serials, 'session': request.session['user_id']})
        url_second = 'http://127.0.0.1:9000/api/v1/image/result/'
        headers = {'Content-type': 'application/json'}
        response_second = requests.post(url_second, headers=headers, data=payload)
        answer = response_second.json()
        print(answer)
        if not answer:
            return redirect('/error')
    else:
        return redirect('/not_home1337')
    return render(request, 'main/main.html')


def notmainpage(request):
    return render(request, 'main/notmain.html')


@login_required
def mail(request):
    email_checker = request.POST.get("email_user")
    if email_checker:
        mail_user = send_mail('UHUUUU!', 'Thank you for visiting our site!', 'svetadoroshuk123@gmail.com', [email_checker, ],
                         fail_silently=False)
        if mail_user:
            messages.success(request, 'Working...')
        else:
            messages.error(request, 'Bad...')
    return render(request, 'main/main.html')


class RegisterFormView(FormView):
    form_class = CustomUserCreationForm
    success_url = '/login'
    template_name = "main/reg.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "main/log.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        url_second = 'http://127.0.0.1:9000/api/v1/image/checker/'
        requests.get(url_second)
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


def user_delete(request):
    search_query = request.GET.get('break', '')
    request.session['user_id'] = search_query
    user = CustomUser.objects.get(id=request.session['user_id'])
    payload = json.dumps({'name_of_user': user.username})
    url_second = 'http://127.0.0.1:9000/api/v1/image/del_bad_user/'
    responce = requests.get(url_second, data=payload)
    answer = responce.json()
    if answer:
        try:
            del request.session['user_id']
            return redirect('/changePassword')
        except KeyError:
            return redirect('/error')

    return render(request, 'main/log.html')




