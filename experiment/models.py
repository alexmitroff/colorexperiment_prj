from django.db import models
from PIL import Image as Img
import StringIO

# Create your models here.

class UserInfo(models.Model):
    GENDER_CHOISES = (
            (0, u"Мужской"),
            (1, u"Женский"),
            )

    EDU_TYPES_CHOISES = (
            (0, u"Гумунитарный"),
            (1, u"Технический"),
            )

    EDU_CHOISES = (
            (0, u"Отсутвует"),
            (1, u"Среднее"),
            (2, u"Среднее специальное"),
            (3, u"Высшее профессиональное"),
            )

    lastname = models.CharField( u"фамилия", max_length=50)
    firstname = models.CharField( u"имя", max_length=50) 
    gender = models.IntegerField( u"пол", default=0, 
            choices=GENDER_CHOISES )
    age = models.PositiveIntegerField( u"возраст", default=0)
    edu_type = models.IntegerField( u"тип образования", 
            default=0, choices=EDU_TYPES_CHOISES )
    edu = models.IntegerField( u"образование", 
            default=0, choices=EDU_CHOISES)
    art_exp = models.BooleanField(u"художественная подготовка",
            default=False)
    edu_prof = models.CharField( u"профиль подготовки", 
            max_length=140)
    email = models.EmailField(u"электронная почта", max_length=254)
    phone = models.PositiveIntegerField( u"телефон", blank=True, null=True)
    cinema_freq = models.PositiveIntegerField( u"частота походов в кинотеатр", default=0)
    cinema_genre = models.CharField( u"любимый жанр кино", max_lenght=140)

    class Meta:
        ordering = ['lastname', 'firstname']
        verbose_name = u"Информация о подопытном"
        verbose_name_plural = u"Информация о подопытных"

    def __str__(self):
        return "%s %s" % (self.lastname, self.firstname)

class Stimul(models.Model):
    pos = models.PositiveIntegerField( u"позиция",
            default=0)
    show = models.BooleanField(u"доступен",
            default=True)
    user = models.ForeignKey("UserInfo",
            on_delete=models.CASCADE ) 
    name = models.CharField( u"Название", max_length=50)

    class Meta:
        ordering = ['show', 'pos']
        verbose_name = u"Информация о подопытном"
        verbose_name_plural = u"Информация о подопытных"
    
    def __str__(self):
        status = u"доступен"
        if self.show:
            status = u"скрыт"
        return "%s | %s" % (self.name, status)

class ImageType(models.Model):
    pos = models.PositiveIntegerField( u"позиция",
            default=0)
    name = models.CharField( u"Название", max_length=50)
    class Meta:
        ordering = ['pos']
        verbose_name = u"Тип изображения"
        verbose_name_plural = u"Типы изображений"
    
    def __str__(self):
        return self.name

class Image(models.Model):
    itype = models.ForeignKey("ImageType", 
            on_delete=models.CASCADE)
    img = models.ImageField()
    class Meta:
        ordering = ['itype']
        verbose_name = u"Изображение"
        verbose_name_plural = u"Изображения"
    def __str__(self):
        return self.itype.name
