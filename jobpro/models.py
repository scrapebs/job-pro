from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

#Extended UserManager
class MyUserManager(BaseUserManager):
    def create_user(self, email, account_type, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            account_type=account_type,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, account_type, username, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            account_type=account_type,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Extended User Model
class User(AbstractUser):
    EMPLOYEE = 'EM'
    ORGANISATION = 'OR'
    ACOUNTS_TYPE_CHOICES = (
        (EMPLOYEE, 'Соискатель'),
        (ORGANISATION, 'Организация')
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=False,
    )
    account_type = models.CharField(max_length=2, choices=ACOUNTS_TYPE_CHOICES, default=EMPLOYEE)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    REQUIRED_FIELDS = ['account_type', 'email']

    def __str__self(self):
        return self.username + '(' + self.account_type + ')'
        
class OrgInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    description = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    actual = models.BooleanField(default=True)
    organisation = models.OneToOneField(auth.get_user_model(), related_name='info', on_delete=models.CASCADE)

    def __str__(self):
        return  self.name

class Vacancy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(blank=True)
    salary = models.IntegerField(default=60000)
    actual = models.BooleanField(default=True)
    owner = models.ForeignKey(auth.get_user_model(), related_name='vacancies', on_delete=models.CASCADE)
    org_info = models.ForeignKey('jobpro.OrgInfo', related_name='orginfo', on_delete=models.CASCADE)
    AVTO = 'AV'
    BANK = 'BA'
    SECURE = 'SE'
    SPORT = 'SP'
    IT = 'IT'
    SCIENCE = 'SC'
    TRADE = 'TR'
    LAWYERS = 'LA'
    PROFESSION_CHOICES = (
        (AVTO, 'Автомобильный бизнес'),
        (BANK, 'Банки, инвестиции'),
        (SECURE, 'Безопасность'),
        (SPORT, 'Спорт'),
        (IT, 'Информационные технологии, интернет, телеком'),
        (SCIENCE, 'Наука, образование'),
        (TRADE, 'Продажи'),
        (LAWYERS, 'Юристы')
    )
    profession = models.CharField(max_length=2,
                                      choices=PROFESSION_CHOICES,
                                      default=AVTO)

    def __str__(self):
        return self.name

class FavouriteVacancy(models.Model):
    user = models.ForeignKey(auth.get_user_model(), related_name='favourite_vacancy', on_delete=models.CASCADE)
    vacancy = models.ForeignKey('jobpro.Vacancy', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + '->' + self.vacancy.name

class Cv(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=40, blank=True)
    email = models.CharField(max_length=40, blank=True)
    created_date = models.DateTimeField(blank=True)
    actual = models.BooleanField(default=True)
    owner = models.ForeignKey(auth.get_user_model(), related_name='cv', on_delete=models.CASCADE)

    def __str__(self):
        return  self.name
        
class FavouriteCv(models.Model):
    user = models.ForeignKey(auth.get_user_model(), related_name='favourite_cv', on_delete=models.CASCADE)
    cv = models.ForeignKey('jobpro.Cv', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + '->' + self.cv.name