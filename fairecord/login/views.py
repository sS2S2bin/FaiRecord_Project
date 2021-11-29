from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse


def index(request):
 return HttpResponse("Hello, User. You must log in.")

