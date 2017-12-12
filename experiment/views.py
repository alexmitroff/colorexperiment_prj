from django.shortcuts import render
from experiment.forms import UserInfoForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect

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

def submit(request):
    if request.method == 'POST':
        print(request.POST)
        stimul = Stimul.objects.get(pk = int(request.POST['stimul']))
        
        profile, p_created = UserInfo.objects.get_or_create(
                email = request.POST['email'],
                defaults = {
                    'lastname':request.POST['lastname'],
                    'firstname':request.POST['firstname'],
                    'gender':request.POST['gender'],
                    'age':request.POST['age'],
                    'edu_type':request.POST['edu_type'],
                    'edu':request.POST['edu'],
                    'art_exp':request.POST['art_exp'],
                    'edu_prof':request.POST['edu_prof'],
                    'phone':request.POST['phone'],
                    'cinema_freq':request.POST['cinema_freq'],
                    'cinema_genre':request.POST['cinema_genre'],
                    }
                )
        
        images = Image.objects.filter(stimul = stimul)
        
        for image in images:
            answer, a_created = Answer.objects.get_or_create(
                user = profile,
                stimul = stimul,
                defaults = {
                    'image':image,
                    'pos':request.POST['images['+str(image.id)+']']
                    }
                )
            if a_created == False:
                return HttpResponse('1')

        return HttpResponse('0')
    else:    
        return HttpResponseRedirect('/')
