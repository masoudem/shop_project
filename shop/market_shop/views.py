from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, reverse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from .forms import ShopForm
from django.urls import reverse_lazy
from .models import CustomUser, Shop
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .access import ActiveOnlyMixin


class PanelView(ActiveOnlyMixin, TemplateView):
    template_name = 'shop_panel/panel.html'


class CreateShop(ActiveOnlyMixin, CreateView):
    template_name = 'shop_panel/create_shop.html'
    form_class = ShopForm
    success_url = "/shop/panel/"

    def form_valid(self, form):
        shop = form.save(commit=False)
        shop.owner = CustomUser.objects.get(email=self.request.user)
        return super(CreateShop, self).form_valid(form)
    
    def get_queryset(self):
        return Shop.objects.filter(owner__email = self.request.user, shop_status = 'not')
        
    
    def get(self, request, **kwargs):
        
        if self.get_queryset():
            return super(CreateShop, self).handle_no_permission()
        else:
            return super().get(request, **kwargs)
        


class ShopListView(ActiveOnlyMixin, ListView):
    model = Shop
    template_name = 'shop_panel/shop_list.html'
    paginate_by = 100

    # def get(self, request, *args, **kwargs):
    #     shop = Shop.objects.filter(owner__email = request.user)
    #     print(shop)
    #     return (shop)
    def get_queryset(self):
        shop = Shop.objects.filter(
            owner__email=self.request.user).filter(shop_status='act')
        return shop


class UpdateShop(ActiveOnlyMixin, UpdateView):
    model = Shop
    fields = '__all__'
    template_name = 'shop_panel/update_shop.html'
    success_url = '/shop/shop_list/'


    def form_valid(self, form):
        shop = form.save(commit=False)
        shop.shop_status = 'pub'
        return super(UpdateShop, self).form_valid(form)
    # def get_queryset(self):
    #     id = (self.kwargs['pk'])
    #     return Shop.objects.get(pk =id).update(shop_status='act')


class DeleteShop(ActiveOnlyMixin, UpdateView):
    model = Shop
    fields = ['shop_type']
    template_name = 'shop_panel/delete_shop.html'
    success_url = '/shop/shop_list/'
    
    def form_valid(self, form):
        shop = form.save(commit=False)
        shop.shop_status = 'del'
        return super(DeleteShop, self).form_valid(form)
