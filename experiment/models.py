from django.db import models

# Create your models here.

class UserInfo(models.Model):
    GENDER_CHOISES = (
            (0, u"Мужской"),
            (1, u"Женский"),
            )

    lastname = models.CharField( u"фамилия", max_length=50)
    firstname 
    gender = models.IntegerField( u"пол", default=0, choices=GENDER_CHOISES )
    age
    edu_type
    edu
    art_exp
    edu_prof
    email
    phone
    cinema_freq
    cinema_genre

    class Meta:

    def __str__(self):
        return "%s %s" % (self.lastname, self.firstname)

