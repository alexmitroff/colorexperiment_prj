from django.shortcuts import render
from experiment.forms import UserInfoForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from experiment.models import *
# Create your views here.

def index(request):
    template = "pages/index.html"
    form = UserInfoForm()
    stimul = Stimul.objects.filter(show=True)[0]
    images = Image.objects.filter(stimul=stimul).order_by('?')
    count = images.count()
    var = {
            'form':form,
            'stimul':stimul,
            'images':images,
            'img_count':count,
            }
    return render(request, template, var)

def submit(request):
    if request.method == 'POST':
        print(request.POST)
        stimul = Stimul.objects.get(pk=int(request.POST['stimul']))
        profile, p_created = UserInfo.objects.get_or_create(
                email = request.POST['email'],
                defaults = {
                    'lastname':request.POST['lastname'],
                    'firstname':request.POST['firstname'],
                    'gender':int(request.POST['gender']),
                    'age':int(request.POST['age']),
                    'edu_type':int(request.POST['edu_type']),
                    'edu':int(request.POST['edu']),
                    'art_exp':int(request.POST['art_exp']),
                    'edu_prof':request.POST['edu_prof'],
                    'cinema_freq':int(request.POST['cinema_freq']),
                    'cinema_genre':request.POST['cinema_genre'],
                    })
        images = Image.objects.filter(stimul=stimul)
        for image in images:
            a, a_created = Answer.objects.get_or_create(
                    stimul = stimul,
                    user = profile,
                    image = image,
                    defaults = {
                        'pos': int(request.POST['images['+str(image.id)+']']),
                        }
                    )

            if a_created == False:
                return HttpResponce('')
                
        return HttpResponse('OK!')
    else:
        return HttpResponseRedirect('/')
