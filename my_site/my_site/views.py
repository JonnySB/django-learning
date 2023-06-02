from django.http.response import HttpResponse


def home(response):
    return HttpResponse('Home View')
