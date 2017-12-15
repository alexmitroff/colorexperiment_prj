from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from experiment.forms import *
from experiment.models import *

from excel_response import ExcelResponse



# Create your views here.

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def index(request):
    template = "pages/index.html"
    try:
        stimuli_passed = Stimul.objects.filter(stimuluspassed__user = request.user)
        sp_vl = stimuli_passed.values_list('id')
        stimuli = Stimul.objects.filter(show=True).exclude(id__in = sp_vl)
    except:
        stimuli_passed = []
        stimuli = Stimul.objects.filter(show=True)
    var = {
            'stimuli_n':stimuli,
            'stimuli_p':stimuli_passed,
            }
    return render(request, template, var)

@login_required
def profile(request):
    template = "pages/profile.html"
    user = request.user
    u_form = UserForm(instance=user)
    ui, ui_created = UserInfo.objects.get_or_create(
            user=user,
            )
    ui_form = UserInfoForm(instance=ui)
    var = {
            'u_form':u_form,
            'ui_form':ui_form,
            }
    return render(request, template, var)


@login_required
def submit(request):
    if request.method == 'POST':
        print(request.POST)
        stimulus = get_object_or_404(Stimul, pk = int(request.POST['stimulus']))
        images = Image.objects.filter(stimul = stimulus)
        passed, p_created = StimulusPassed.objects.get_or_create(
                user=request.user,
                stimulus = stimulus,
                )

        if p_created == False:
            return HttpResponse('1')

        for image in images:
            a, a_created = Answer.objects.get_or_create(
                    user = request.user,
                    stimulus = stimulus,
                    image = image,
                    defaults = {
                        'pos': int(request.POST['images['+str(image.id)+']']),
                        }
                    )

            if a_created == False:
                return HttpResponse('1')
                
        return HttpResponse('0')
    else:
        return HttpResponseRedirect('/stimulus/'+stimulus.id)

@login_required
def change_user(request):
    if request.method == 'POST':
        print(request.POST)
        user = request.user
        user.email = request.POST['email']
        user.last_name = request.POST['last_name']
        user.first_name = request.POST['first_name']
        user.save()
        return HttpResponse('1')
    else:
        return HttpResponse('0')

@login_required
def change_userinfo(request):
    if request.method == 'POST':
        print(request.POST)
        user = request.user
        ui, ui_created = UserInfo.objects.get_or_create(user=user,)
        ui.gender = int(request.POST['gender'])
        ui.age = int(request.POST['age'])
        ui.edu_type = int(request.POST['edu_type'])
        ui.edu = int(request.POST['edu'])
        ui.art_exp = int(request.POST['art_exp'])
        ui.edu_prof = request.POST['edu_prof']
        ui.phone = request.POST['phone']
        ui.cinema_freq = int(request.POST['cinema_freq'])
        ui.cinema_genre = request.POST['cinema_genre']
        ui.save()
        return HttpResponse('1')
    else:
        return HttpResponse('0')



@login_required
def result(request, stimulus_id):
    user = -1
    stimul = get_object_or_404(Stimul, pk = stimulus_id)
    answers = Answer.objects.filter(stimul = stimul)
    
    users = answers.distinct('user').values('user')

    s_fields = Stimul._meta.get_fields()
    
    print(users)
    return HttpResponse('Ok!')

@login_required
def stimulus(request, stimulus_id):
    template = 'pages/stimulus.html'
    stimulus = get_object_or_404(Stimul, pk = stimulus_id)
    images = Image.objects.filter(stimul = stimulus).order_by('?')
    var = {
            'stimulus':stimulus,
            'images':images,
            }
    return render(request, template, var)
