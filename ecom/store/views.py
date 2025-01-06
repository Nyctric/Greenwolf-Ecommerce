from django.shortcuts import render, redirect
from .models import Category, Product, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForms
from django import forms
from django.db.models import Q
import json
from cart.cart import Cart

from .forms import ModelUploadForm
from .models import UploadedModel



def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains = searched))

        if not searched:
             messages.success(request, "No se encontaron resultados" )
             return render(request, "search.html", {})
        else:
            return render(request, "search.html", {'searched':searched})

        return render(request, "search.html", {'searched':searched})

    else:
        return render(request, "search.html", {})




def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForms(request.POST or None, instance=current_user)


        if form.is_valid():
            user_form.save()

            messages.success(request, "La informacion ha sido actualizado" )
            return redirect('home')
        return render(request, "update_info.html", {'form':form})
    else:
        messages.success(request, "Debes logearte para acceder a la pagina " )
        return redirect('home')

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "Tu contraseña ha sido actualizada,por favor inicia sesion nuevamente")
                #login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
            

        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {'form':form})
    else: 
         messages.success(request, "Debes logearte para acceder a la pagina " )
         return redirect('home')


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "El usuario ha sido actualizado" )
            return redirect('home')
        return render(request, "update_user.html", {'user_form':user_form})
    else:
        messages.success(request, "Debes logearte para acceder a la pagina " )
        return redirect('home')

    

def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {"categories":categories})



def category(request, foo):
    # Reemplaza guion  con espacio
    foo = foo.replace('-',' ')
    # toma la categoria desde el URL
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html',{'products':products, 'category': category })

    except:
        messages.success(request, ("La categoria no existe"))
        return redirect('home')

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})
    


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {'products':products})

def about(request):
    return render(request, "about.html", {})

def login_user(request):
    if request.method == "POST": 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Modificaciones del carrito
            current_user =  Profile.objects.get(user__id=request.user.id)

            #obtener los productos guardados desde la base de datos
            saved_cart = current_user.old_cart
            if saved_cart:
                #convertir en diccionario utilizando JSON
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key,value in  converted_cart.items():
                    cart.db_add(product=key, quantity=value)
            





            messages.success(request, ("Has iniciado sesion correctamente"))
            return redirect('home')
        
        else:
            messages.success(request, ("Usuario o contraseña incorrectos, intenta nuevamente"))
            return redirect('login')


    else:
        return render(request,'login.html',{})
    
  

def logout_user(request):
    logout(request)
    messages.success(request,(" Seras reenviado a la pagina de Inicio") )
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,(" Te has registrado correctamente, completa la info") )
            return render('update_info')
        else: 
            messages.success(request,("No se ha podido llevar acabo el registro, por favor intenta nuevamente") )
            return redirect('register')

    return render(request,'register.html',{'form':form})



# SUBIDA DE ARCHIVO

def upload_model(request):
    if request.method == 'POST':
        form = ModelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Guarda el archivo en el servidor
            # No se redirige a ninguna otra página; se recarga la misma página
    else:
        form = ModelUploadForm()
    return render(request, 'upload_model.html', {'form': form})


