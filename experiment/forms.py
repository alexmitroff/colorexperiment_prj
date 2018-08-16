from django.forms import ModelForm
from experiment.models import UserInfo
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
                'email',
                'last_name',
                'first_name',
                ]

class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = [
                'gender',                  
                'age',                  
                'edu_type',                  
                'edu',                  
                'art_exp',                  
                'edu_prof',                  
                'phone',                  
                'cinema_freq',                  
                'cinema_genre',                  
                ]
