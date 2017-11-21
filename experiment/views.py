from django.shortcuts import render
from experiment.forms import UserInfoForm

from experiment.models import *

# Create your views here.

def index(request):
    template = "pages/index.html"
    form = UserInfoForm()
    stimul = Stimul.objects.filter(show=True)[0]
    images = Image.objects.filter(stimul = stimul)
    var = {
            'form':form,
            'stimul':stimul,
            'images':images,
            }
    return render(request, template, var)
