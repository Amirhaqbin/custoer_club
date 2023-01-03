from turtle import mode
from django.db import models
from app.models import CustomUser
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import uuid

DURATION_CHOICESE = {
    
    ( 30 , 'month'),
    ( 1, 'day'),
    ( 7, 'week'),
    ( 365, 'year'),
    
}



class Gift(models.Model):
    id = models.BigAutoField(primary_key=True,unique=True)
    title = models.CharField(verbose_name='نام جایزه',max_length=300, null=True, blank=True)
    slug = models.SlugField(allow_unicode=True, unique=True, null=False)
    score = models.IntegerField(verbose_name='امتیاز', default=0)
    allowed_to_used = models.PositiveSmallIntegerField(verbose_name='تعداد دسترسی به جوایز')
    allowed_to_used_duration = models.IntegerField(verbose_name='مدت اعتبار', choices=DURATION_CHOICESE)
    # expired_duration = models.JSONField(verbose_name='{تعداد:مدت زمان}',null=True, blank=True, default=dict)
    detail = models.CharField(max_length=2000, verbose_name='جزئیات ')
    image = models.ImageField(verbose_name='عکس جایزه',upload_to='project/static')
    create_at= models.DateTimeField(verbose_name='تاریخ ساخت جایزه',auto_now_add=True)
    worth = models.DecimalField(verbose_name='ارزش',max_digits=12, decimal_places=1)
    

    def __str__(self):
        return self.title
    
    # def get_api_like_url(self):
    #     return reverse("gifts:Score-api", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'جوایز'
        verbose_name_plural = 'جوایز ها'



class Profile(models.Model):
    profile = models.CharField(max_length=100, default='profile', blank=True, null=True)
    customer = models.OneToOneField(CustomUser, on_delete= models.CASCADE, related_name= 'customuser')
    is_gold = models.BooleanField(default=False)
    score_user = models.IntegerField(verbose_name='تعداد امتیاز', default=0)

    # def __str__(self):
    #     return self.profile
    def __str__(self):
        return self.profile

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها '


class Log(models.Model):
    logs = models.CharField(max_length=100, null=True, blank=True, default="history")
    gift = models.ForeignKey(Gift, related_name='log',verbose_name='نام جایزه انتخاب شده',on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='log',verbose_name='کاربر',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True ,verbose_name='تاریخ اضافه شدن ')
    score_log = models.IntegerField(null=True, blank=True)


    def is_active(self):
        timezone.now()
    
    def __str__(self):
        return self.logs

    # def save(self, *args, **kwrgs):
    #     self.user = self.user+2
    #     self.user.save()
    #     super().save(*args, **kwrgs)

    # def save(self, *args, **kwrgs):
    #     idnumber = int(self.user.id_number)
    #     self.user.id_number = self.user.id_number+"1"
    #     self.user.save()
    #     super().save(*args, **kwrgs)    








    # def save(self, *args, **kwrgs):
    #     self.score_user = self.score_user+1
        

    #     super().save(*args, **kwrgs)

    # def delete(self, *args, **kwrgs):
    #     self.scor_user = self.score_user-1
        
    #     super().save(*args, **kwrgs)
