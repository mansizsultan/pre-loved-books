from django.shortcuts import render, redirect 
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    product = Product.objects.all()

    context = {
        'author': 'Kami adalah destinasi utama bagi para pencinta buku yang mencari harta karun literatur dengan harga terjangkau. Di sini, setiap buku memiliki cerita yang kaya dan penuh kenangan. Toko kami berkomitmen untuk memberikan kesempatan kedua bagi buku-buku yang sudah melewati perjalanan hidupnya, agar tetap dapat dinikmati oleh pembaca baru.',
        'description': 'Selamat berbelanja',
        'products': product,
    }
    
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def clear_table(request):
    Product.objects.all().delete()
    return redirect('main:show_main')

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")