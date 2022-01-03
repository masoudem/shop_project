from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, reverse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import FormView, View
from .forms import ShopForm
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib import messages



class PanelView(LoginRequiredMixin,TemplateView):
    template_name = 'shop_panel/panel.html'
    