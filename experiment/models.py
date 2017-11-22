from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from PIL import Image as Img
from io import StringIO

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

    ART_CHOISES = (
            (0, u"Нет"),
            (1, u"Да"),
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
    art_exp = models.PositiveIntegerField(u"художественная подготовка",
            default=0, choices=ART_CHOISES)
    edu_prof = models.CharField( u"профиль подготовки", 
            max_length=140)
    email = models.EmailField(u"электронная почта", max_length=254)
    phone = models.PositiveIntegerField( u"телефон", blank=True, null=True)
    cinema_freq = models.PositiveIntegerField( u"частота походов в кинотеатр", default=0)
    cinema_genre = models.CharField( u"любимый жанр кино", max_length=140)

    class Meta:
        ordering = ['lastname', 'firstname']
        verbose_name = u"Информация о подопытном"
        verbose_name_plural = u"Информация о подопытных"

    def __str__(self):
        return "%s %s" % (self.lastname, self.firstname)


class StimulType(models.Model):
    pos = models.PositiveIntegerField( u"позиция",
            default=0)
    name = models.CharField( u"Название", max_length=50)
    class Meta:
        ordering = ['pos']
        verbose_name = u"Тип стимула"
        verbose_name_plural = u"Типы стимулов"
    
    def __str__(self):
        return self.name

class Stimul(models.Model):
    pos = models.PositiveIntegerField( u"позиция",
            default=0)
    show = models.BooleanField(u"доступен",
            default=True)
    stype =  models.ForeignKey("StimulType", 
            on_delete=models.CASCADE, default=0)
    name = models.CharField( u"Название", max_length=50)

    class Meta:
        ordering = ['show', 'pos']
        verbose_name = u"Стимул"
        verbose_name_plural = u"Стимулы"
    
    def __str__(self):
        status = u"скрыт"
        if self.show:
            status = u"доступен"
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


def image_path(instance, filename):
    filename = filename.replace(" ", "")
    if len(filename) > 100:
        filename = filename[:99]
    return "{0}/{1}".format(instance.itype.id, filename)

class Image(models.Model):
    stimul = models.ForeignKey("Stimul",
            on_delete=models.CASCADE, default=0 ) 
    itype = models.ForeignKey("ImageType", 
            on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_path)
    
    class Meta:
        ordering = ['itype']
        verbose_name = u"Изображение"
        verbose_name_plural = u"Изображения"
    
    def save(self, *args, **kwargs):
        try:
            this = Image.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
                self = optimize_image(self)
        except:
            pass
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return self.itype.name

@receiver(pre_delete, sender=Image)
def image_delete(sender, instance, **kwargs):
    instance.image.delete(False)

class Answer(models.Model):
    pos = models.PositiveIntegerField( u"позиция",
            default=0)
    user = models.ForeignKey("UserInfo",
            on_delete=models.CASCADE ) 
    stimul = models.ForeignKey("Stimul",
            on_delete=models.CASCADE ) 
    image = models.ForeignKey("Image",
            on_delete=models.CASCADE )
    class Meta:
        ordering = ['stimul','user','pos']
        verbose_name = u'Ответ'
        verbose_name_plural = u'Ответы'
    def __srt__(self):
        return "%s %s %s" % (self.stimul, self.user, self.image)
