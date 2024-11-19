from django.shortcuts import render, redirect
from main.forms import ItemForm
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    
    context = {
        'npm' : '2306152424',
        'name': request.user.username,
        'class': 'PBP C',
        
        'last_login': request.COOKIES.get('last_login', 'Not logged in'),  # Safe access to the cookie
    }

    return render(request, "main.html", context)

def create_item_entry(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item_entry = form.save(commit=False)
        item_entry.user = request.user
        item_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_item_entry.html", context)

def show_xml(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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
          messages.error(request, "Invalid username or password. Please try again.")
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_item(request, id):
    # Get item entry berdasarkan id
    item = Item.objects.get(pk = id)

    # Set item entry sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def delete_item(request, id):
    # Get item berdasarkan id
    item = Item.objects.get(pk = id)
    # Hapus item
    item.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def show_products(request):
    item_entries = Item.objects.all()
    context = {
        'npm' : '2306152424',
        'name': request.user.username,
        'class': 'PBP C',
        'item_entries': item_entries,
        'last_login': request.COOKIES.get('last_login', 'Not logged in'), 
    }

    return render(request, "products.html", context)

def view_cart(request):
    data = Item.objects.all()
    item_entries = Item.objects.filter(user=request.user)
    context = {
        'npm' : '2306152424',
        'name': request.user.username,
        'class': 'PBP C',
        'item_entries': item_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def buy_products(request):
    # Simulating inventory items
    chest_items = [None] * 54  # Empty slots (you can populate with images later)
    inventory_items = [None] * 27  # Empty slots

    # Pass the items to the template
    context = {
        'chest_items': chest_items,
        'inventory_items': inventory_items,
    }
    return render(request, 'inventory_2.html', context)

@csrf_exempt
@require_POST
def add_item_entry_ajax(request):
    name =  strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
   
    stock = request.POST.get("stock")
    imutness_rating = request.POST.get("imutness_rating")
    user = request.user

    new_item = Item(
        name=name, price=price,
        description=description,
        stock=stock,
        imutness_rating=imutness_rating,
        user=user
    )
    new_item.save()

    return HttpResponse(b"CREATED", status=201)

from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import Item

@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_item = Item.objects.create(
                user=request.user,
                name=data["name"],
                price=int(data["price"]),
                description=data["description"],
                stock=int(data["stock"]),
                imutness_rating=float(data["imutness_rating"])
            )

            new_item.save()

            return JsonResponse({"status": "success"}, status=200)
        except (KeyError, ValueError) as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=401)
