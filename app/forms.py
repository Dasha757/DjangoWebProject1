"""
Definition of forms.
"""

from django.db import models
from .models import Comment
from .models import Blog

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', min_length=2, max_length=100)
    name.widget.attrs.update({'id': 'bu1'})
    city = forms.CharField(label='Город', min_length=2, max_length=100)
    city.widget.attrs.update({'id': 'bu2'})
    job = forms.CharField(label='Ваша любимая выпечка:', min_length=2, max_length=100)
    job.widget.attrs.update({'id': 'bu3'})
    gender = forms.ChoiceField(label='Пол',
                             choices=[('1', 'Мужской'), ('2', 'Женский')],
                             widget=forms.RadioSelect, initial=1)
    coffee = forms.ChoiceField(label='Вы пьёте кофе',
                               choices=(('1', 'Каждый день'),
                               ('2', 'Несколько раз в неделю'),
                               ('3', 'Несколько раз в месяц'),
                               ('4', 'Не пью')), initial=1)
    coffee.widget.attrs.update({'id': 'bu4'})
    notice = forms.BooleanField(label='Хотите получать рассылку?',
                                required=False)
    email = forms.EmailField(label='Ваш e-mail', min_length=7)
    email.widget.attrs.update({'id': 'bu5'})
    message = forms.CharField(label='Оставьте отзыв:',
                              widget=forms.Textarea(attrs={'rows':12, 'cols':20}))
    message.widget.attrs.update({'id': 'bu6'})

class CommentForm(forms.ModelForm):
     class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}

class BlogForm(forms.ModelForm):
     class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}