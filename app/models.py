from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import ugettext as _
import uuid



class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, id_number, mobile_phone, address, zip_code, password=None, is_staff=False, is_active=True):
        if not first_name:
            raise ValueError("User must have an id number")
        if not last_name:
            raise ValueError("User must have a first_name")
        if not id_number:
            raise ValueError("User must have a last_name")
        if not mobile_phone:
            raise ValueError("User must have a mobile_phone")
        if not address:
            raise ValueError("User must have an address")
        if not zip_code:
            raise ValueError("User must have a zip_code")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(id_number=id_number)
        user.first_name = first_name
        user.last_name = last_name
        user.mobile_phone = mobile_phone
        user.address = address
        user.zip_code = zip_code
        user.set_password(password)  # changes password to hash
        user.is_staff = is_staff
        user.is_active = is_active
        user.save(using=self._db)
        return user
        
    def create_superuser(self, first_name, last_name, id_number, mobile_phone, address, zip_code, password=None, **extra_fields):
        if not first_name:
            raise ValueError("User must have an id number")
        if not last_name:
            raise ValueError("User must have a first_name")
        if not id_number:
            raise ValueError("User must have a last_name")
        if not mobile_phone:
            raise ValueError("User must have a mobile_phone")
        if not address:
            raise ValueError("User must have an address")
        if not zip_code:
            raise ValueError("User must have a zip_code")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(id_number=id_number)
        user.first_name = first_name
        user.last_name = last_name
        user.mobile_phone = mobile_phone
        user.address = address
        user.zip_code = zip_code
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
   




DEGREE_CHOICES = {

    ('Undergraduate', 'زیر دیپلم'),
    ('Bachelor', 'لیسانس'),
    ('Master', 'فوق لیسانس'),
    ('Phd', 'دکترا'),

}


class CustomUser(AbstractUser):
    
    GENDER = (
        ('M', 'مرد'),
        ('F', 'زن'),
    )

    # uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    id_number = models.CharField(verbose_name='شماره ملی', max_length=10, unique=True)
    first_name = models.CharField(verbose_name='نام', max_length=150)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=150)
    gender = models.CharField(verbose_name='جنسیت', max_length=10,default= '', choices=GENDER)
    birth_date = models.DateTimeField(verbose_name= 'تاریخ تولد', null=True, blank=True)
    mobile_phone = models.CharField(verbose_name='تلفن همراه', max_length=11)
    telephone_number = models.CharField(verbose_name='تلفن ثابت', max_length=11, null=True, blank=True)
    email = models.EmailField(verbose_name= 'آدرس ایمیل', unique=True, null=True, blank=True)
    address = models.CharField(verbose_name='آدرس', max_length=1080)
    zip_code = models.CharField(verbose_name='کد پستی', max_length=10)
    password = models.CharField(verbose_name='رمز عبور', max_length=128)
    create_at = models.DateTimeField(verbose_name='تاریخ ساخت کاربر', auto_now_add=True )
    updated_at = models.DateTimeField(verbose_name='آخرین به روز رسانی', auto_now=True)
    family_member = models.CharField(verbose_name='عضو خانواده',max_length=128, null=True, blank=True)
    social_media = models.CharField(verbose_name='فضای مجازی', max_length= 68 ,null=True, blank=True)                
    degree = models.CharField(verbose_name='مدرک تحصیلی', max_length=15, blank=True, null=True, choices=DEGREE_CHOICES)
    store = models.CharField(verbose_name='فروشگاه',max_length=128, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'id_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile_phone', 'address', 'zip_code',]

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        ordering = ('last_name', 'first_name', 'id_number')
    
    def __str__(self) -> str:
        return f'{self.get_full_name()} ({self.username})'


   
class Store(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_store')
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    square_meter = models.FloatField()

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'مغازه'
        verbose_name_plural = 'مغازه ها ' 


#######################################


FAMILY_CHOICES = {

    ('Partner', 'همسر'),
    ('Child', 'فرزند')

}


class FamilyMember(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_family')
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    relation = models.CharField(max_length=7, choices=FAMILY_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}({self.relation})'    

#######################################

OCASION_CHOICES = {
    
        ('birthday', 'birthday'),
        ('anniversary', 'anniversary')
}

class ImportantDate(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_important_day')
    date = models.DateTimeField()
    occasion = models.CharField(max_length=11, choices=OCASION_CHOICES)
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='family_member')

    def __str__(self):
        return str(self.date)


