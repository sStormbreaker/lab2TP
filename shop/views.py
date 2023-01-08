from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase, Discount

plusDiscount = 0.5

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()

        # Purchase.objects.all().delete()
        # for p in Purchase.objects.all():
        #     print(p.person)

        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')


