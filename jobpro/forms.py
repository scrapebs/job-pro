from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User, Vacancy, Cv, OrgInfo

class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ('name', 'description', 'profession', 'salary')


class CvForm(forms.ModelForm):

    class Meta:
        model = Cv
        fields = ('name', 'description', 'phone', 'email')


class OrgInfoForm(forms.ModelForm):

    class Meta:
        model = OrgInfo
        fields = ('name', 'address', 'phone', 'email', 'description')


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'account_type')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username','email', 'password', 'account_type', 'is_active')  #is_admin

    def clean_password(self):
        return self.initial["password"]   
