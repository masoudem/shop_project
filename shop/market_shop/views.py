from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView

from .forms import ShopForm, ProductForm, TagForm, CategoryForm
from .models import Basket, CustomUser, Product, Shop

from .access import ActiveOnlyMixin


# shop
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
        return Shop.objects.filter(owner__email=self.request.user, shop_status='not')

    def get(self, request, **kwargs):

        if self.get_queryset():
            return super(CreateShop, self).handle_no_permission()
        else:
            return super().get(request, **kwargs)


class ShopListView(ActiveOnlyMixin, ListView):
    model = Shop
    template_name = 'shop_panel/shop_list.html'
    paginate_by = 4

    def get_queryset(self):
        shop = Shop.objects.filter(
            owner__email=self.request.user).filter(shop_status='act')
        return shop


class ShopDetailView(ActiveOnlyMixin, DetailView):
    model = Shop
    template_name = 'shop_panel/shop_detail.html'


class UpdateShop(ActiveOnlyMixin, UpdateView):
    model = Shop
    form_class = ShopForm
    template_name = 'shop_panel/update_shop.html'
    success_url = '/shop/shop_list/'

    def form_valid(self, form):
        shop = form.save(commit=False)
        shop.shop_status = 'pub'
        return super(UpdateShop, self).form_valid(form)
    


class DeleteShop(ActiveOnlyMixin, UpdateView):
    model = Shop
    fields = ['shop_type']
    template_name = 'shop_panel/delete_shop.html'
    success_url = '/shop/shop_list/'

    def form_valid(self, form):
        shop = form.save(commit=False)
        shop.shop_status = 'del'
        return super(DeleteShop, self).form_valid(form)


# product
class CreateProduct(ActiveOnlyMixin, CreateView):
    template_name = 'shop_panel/create_product.html'
    form_class = ProductForm
    success_url = "/shop/panel/"

    def form_valid(self, form):
        product = form.save(commit=False)
        id = (self.kwargs['pk'])
        product.shop = Shop.objects.get(pk=id)
        return super(CreateProduct, self).form_valid(form)


class CreateCategory(ActiveOnlyMixin, CreateView):
    template_name = 'shop_panel/create_category.html'
    form_class = CategoryForm
    success_url = "/shop/panel/"


class CreateTag(ActiveOnlyMixin, CreateView):
    template_name = 'shop_panel/create_tag.html'
    form_class = TagForm
    success_url = "/shop/panel/"


class BasketListView(ActiveOnlyMixin, ListView):
    model = Basket
    template_name = 'shop_panel/basket_list.html'
    paginate_by = 4

    def get_queryset(self):
        name = self.kwargs["name"]
        basket = Basket.objects.filter(
            basketitem__product__shop__shop_name=name)
        print(basket)

        return basket


class BasketDetailView(ActiveOnlyMixin, UpdateView):
    model = Basket
    template_name = 'shop_panel/basket_detail.html'
    fields = ['basket_status']
    success_url = "/shop/panel/"

    def get_context_data(self, **kwargs):
        ctx = super(BasketDetailView, self).get_context_data(**kwargs)
        print(ctx)
        id = (self.kwargs["pk"])
        print(id)
        ctx['filter'] = Basket.objects.get(pk=id)
        print(ctx)
        return ctx


class BasketStatusView(ActiveOnlyMixin, UpdateView):
    model = Basket
    fields = ['basket_status']
    template_name = 'shop_panel/basket_status.html'
    success_url = "/shop/panel/"


class ProductListView(ActiveOnlyMixin, ListView):
    model = Product
    template_name = 'shop_panel/product_list.html'
    paginate_by = 4

    def get_queryset(self):

        id = self.kwargs['pk']
        product = Product.objects.filter(shop__pk=id)
        print(product)
        return product


class ChartView(ActiveOnlyMixin, DetailView):
    model = Product
    template_name = 'shop_panel/chart.html'

    def get_context_data(self, **kwargs):
        ctx = super(ChartView, self).get_context_data(**kwargs)

        labels = []
        data = []
        price = []
        queryset = Product.objects.filter(shop__pk=self.kwargs['pk'])
        for entry in queryset:
            labels.append(entry.product_name)
            data.append(entry.product_unit)
            price.append(entry.price_per_unit)

        ctx['labels'] = labels
        ctx['data'] = data
        ctx['price'] = price
        return ctx
