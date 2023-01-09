from django.http import HttpResponse
from django.template import loader
from .models import Product


def products(request):
    myproducts = Product.objects.all().values()
    template = loader.get_template('all_products.html')
    context = {
        'myproducts': myproducts,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    myproducts = Product.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myproducts': myproducts,
    }
    return HttpResponse(template.render())


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))