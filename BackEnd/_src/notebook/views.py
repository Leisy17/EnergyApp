from django.shortcuts import render

from .forms import UserForm

# Create your views here.


def home(request):
    form = UserForm()
    context = {
        "my_form": form
    }
    return render(request, "home.html", context)
