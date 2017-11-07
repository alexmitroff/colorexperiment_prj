from django.shortcuts import render
from experiment.forms import UserInfoForm

# Create your views here.

def index(request):
    template = "pages/index.html"
    form = UserInfoForm()
    var = {
            'form':form,
            }
    return render(request, template, var)
