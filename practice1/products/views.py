from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm


# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {'form': form}
    return render(request, 'products/product_create.html', context)


def product_detail_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    # obj = get_object_or_404(Product, id=my_id)
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {'obj': obj}
    return render(request, 'products/product_detail.html', context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../')
    context = {'obj': obj}
    return render(request, 'products/product_delete.html', context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {'objlist': queryset}
    return render(request, 'products/product_list.html', context)