from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from notes.models import Note

def home_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                notes = Note.objects.filter(user=request.user)
                return render(request, 'notes/index.html', {'notes':notes})
            else:
                return render(request, 'home.html', messages.info('Your account is disables'))
        else:
            messages.add_message(request, messages.INFO, 'Authentication Failed!')
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'home.html')
