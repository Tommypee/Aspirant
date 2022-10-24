from django.shortcuts import render, redirect, reverse
from contact.forms import ContactForm
from django.contrib import messages
from contact.models import Ssce
from contact.forms import SsceForm
# Create your views here.

def contact(request):
    form = ContactForm(request.POST or None)
    context = {
       form: 'Form'
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('contact'))
    return render(request, 'general/contact.html', context)

def wacepage(request):
    schools = Ssce.objects.all()
    context = {
        'ssces': schools
    }
    return render(request, 'contact/index.html', context)

def new_candidate(request):
    form = SsceForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            form = form.save(commit = False)
            user = request.user
            form.save()
            return redirect(reverse('add_candidates'))
    return render(request, 'contact/add.html', context)

