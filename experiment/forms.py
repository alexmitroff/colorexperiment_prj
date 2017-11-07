from django.forms import ModelForm
from experiment.models import UserInfo

class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = [
                'lastname',                  
                'firstname',                  
                'gender',                  
                'age',                  
                'edu_type',                  
                'edu',                  
                'art_exp',                  
                'edu_prof',                  
                'email',                  
                'phone',                  
                'cinema_freq',                  
                'cinema_genre',                  
                ]
