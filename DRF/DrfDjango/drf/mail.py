import email
import imaplib
import os

from django.core.mail import send_mail


def put_email(putting_email, ses):
    send_mail('You was attacked!', f'http://127.0.0.1:8000/logout/?break={ses}', 'svetadoroshuk123@gmail.com',
              [putting_email, ],
              fail_silently=False)


def path_remover():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'img\\cam.jpg')
    os.remove(path)
