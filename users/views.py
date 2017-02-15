import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate as auth_authenticate, login as auth_login
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.template.response import TemplateResponse
from django.core.files.storage import default_storage
from django.conf import settings
from registration.backends.hmac.views import ActivationView
from users.forms import DotanerdUserCreationForm, ProfileForm
from questions.models import Profile

from time import time

from base64 import b64decode
from django.core.files.base import ContentFile

class DotanerdActivationView(ActivationView):
    """Two-phase registration custom class. Currntly used ofr registration."""
    def activate(self, *args, **kwargs):
        # This is safe even if, somehow, there's no activation key,
        # because unsign() will raise BadSignature rather than
        # TypeError on a value of None.
        username = self.validate_key(kwargs.get('activation_key'))
        if username is not None:
            user = self.get_user(username)
            if user is not None:
                user.is_active = True
                user.save()
                # create profile object
                profile = Profile()
                profile.user = user
                profile.save()
                return user
        return False

def register(request):
    "Use for simple registration only."
    if request.method == 'POST':
        form = DotanerdUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username', '')
            password = request.POST.get('password1', '')
            user = auth_authenticate(username=username, password=password)

            # create profile object
            profile = Profile()
            profile.user = user
            # profile.photo = json.loads(user_map.identity.data)['photo']
            profile.save()
            auth_login(request, user)
            return HttpResponseRedirect('/users/profile/')
    else:
        form = DotanerdUserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('register.html', token)

@login_required()
def profile(request):
    return render_to_response('profile.html', {'user': request.user, 'timestamp': time() })


def update_profile(request, template_name):
    if request.method == "POST":
        form = ProfileForm(request.user, request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            filename = request.user.username + '_photo.jpg'  # received file name
            #image = form.files.get('photo')
            asd = form.data['uploaded_image'].split(',')[1]
            image_data = b64decode(asd)
            image = ContentFile(image_data, 'whatup.png')
            if image:
                absfilepath = os.path.join(settings.PHOTO_ROOT, filename)
                with default_storage.open(absfilepath, 'wb+') as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)
                form.instance.photo = os.path.join(settings.MEDIA_URL, settings.PHOTO_DIR, filename)
            else:
                form.instance.photo = form.instance.photo.field.get_default()
            form.save()
            return redirect(reverse('profile'))
    else:
        return redirect(reverse('cropping'))
        form = ProfileForm(user=request.user)
    context = {
        'form': form,
    }

    return TemplateResponse(request, template_name, context)


def cropping(request):
    return  render_to_response('cropping.html')