from django.shortcuts import render

# Create your views here.


def all_products(request):
    """ A view to return all products, including sorting and search enquires """
    return render(request, 'products/products.html', context)