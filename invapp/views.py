from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.

# CRUD = Create , Read, Update, Delete

#Home View
def home_view(request):
    return render(request, 'invapp/home.html')

#Create View
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invapp/product_form.html', {'form': form})

#Read View
def product_list_view(request):
    product = Product.objects.all()
    return render(request, 'invapp/product_list.html', {'products':product})

# Update View
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'invapp/product_form.html', {'form': form})

#Delete View
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id = product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invapp/product_confirm_delete.html', {'products':product})
