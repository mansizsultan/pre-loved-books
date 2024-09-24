import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from main.forms import ProductForm
from main.models import Product


@login_required(login_url='/login')
def show_main(request):
    product = Product.objects.filter(user=request.user)

    context = {
        'student_name': 'Sultan Ibnu Mansiz',
        'student_id': 2306275840,
        'student_class': 'PBP D',  
        'description': 'Kami adalah destinasi utama bagi para pencinta buku yang mencari harta karun literatur dengan harga terjangkau. Di sini, setiap buku memiliki cerita yang kaya dan penuh kenangan. Toko kami berkomitmen untuk memberikan kesempatan kedua bagi buku-buku yang sudah melewati perjalanan hidupnya, agar tetap dapat dinikmati oleh pembaca baru.',
        'greet': 'Selamat berbelanja',
        'name': request.user.username,
        'products': product,
        'last_login': request.COOKIES['last_login'],
    }
    
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def clear_table(request):
    Product.objects.all().delete()
    return redirect('main:show_main')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

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