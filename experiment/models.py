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


class Stimul(models.Model):
    pos = models.PositiveIntegerField( u"позиция",
            default=0)
    show = models.BooleanField(u"доступен",
            default=True)
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


def image_path(instance, filename):
    filename = filename.replace(" ", "")
    if len(filename) > 100:
        filename = filename[:99]
    return "{0}/{1}".format(instance.itype.id, filename)

def optimize_image(obj):
    img = Img.open(StringIO.StringIO(obj.image.read()))
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img_width = 500
    img.thumbnail((img_width,
                   img_width * obj.image.height / obj.image.width),
                   Img.ANTIALIAS)
    output = StringIO.StringIO()
    img.save(output, format='JPEG', quality=80)
    output.seek(0)
    obj.image= InMemoryUploadedFile(output,'ImageField',
            "%s.jpg" %obj.image.name.split('.')[0],
            'image/jpeg', output.len, None)
    return obj

class Image(models.Model):
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
