# from view to template, we're using render
from django.shortcuts import render, get_object_or_404
#  but for redirect and all that, these below
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.db import transaction
#  coz these are in the same app, you can use .sth
from .forms import SignUpForm

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    # the code below means after successful log out then it should it the person back to login page otherwise 'homepage'
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'