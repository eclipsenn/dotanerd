# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from questions.models import Profile
from django.utils.translation import ugettext_lazy as _
User = get_user_model()


class DotanerdUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(DotanerdUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class ProfileForm(forms.ModelForm):
    error_messages = {
        'wrong_size': _("The image should be 100x100 pixels."),
    }

    photo = forms.ImageField(label=_('Profile photo'), required=False)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'years_in_dota')

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ProfileForm, self).__init__(*args, **kwargs)

    def clean_photo(self):
        form_data = self.cleaned_data
        photo = form_data['photo']
        if photo and (photo.image.height != 100 or photo.image.width != 100):
            raise forms.ValidationError(
                self.error_messages['wrong_size'],
                code='wrong_size',
            )
        return form_data
