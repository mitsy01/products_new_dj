from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, FormView


from .models import Product, Profile
from .forms import ProductForm, LoginForm, SignUpForm, Profile, ProfileForm, User, UserForm


def get_products(request):
    products = Product.objects.all()
    return render(request=request, template_name="show_prod.html", context=dict(products=products))


def add_products(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("show_prod")
    return render(request=request, template_name="add_prod.html", context=dict(form=form))


def delete_products(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        messages.error(request, "Товар не знайдено.")
        return redirect("show_prod")

    if request.method == 'POST':
        product.delete()
        return redirect("show_prod")

    return render(request, "del_prod.html", {"product": product})


    
def edit_products(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        messages.error(request, "Товар не знайдено.")
        return redirect("show_prod")

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("show_prod")
    else:
        form = ProductForm(instance=product)

    return render(request, "edit_prod.html", {"form": form, "product": product})

    
class ProductsView(ListView):
    def get(self, request: HttpRequest):
        current_page = request.GET.get("page", 1)
        paginator = Paginator(Product.objects.filter(product=request.product).all(), 2)
        page_obj = paginator.get_page(current_page)
        
        return render(request=request, template_name="prod_view.html", context=dict(page_obj=page_obj))
    
def sign_up(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    form = SignUpForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request=request, user=user)
        messages.add_message(request=request, level=messages.SUCCESS, message="Ви зарєєструвались.")
        return redirect("index")
    
    return render(request=request, template_name="sign_up.html", context={"form": form})


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    form = LoginForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            username=form.cleaned_data.get("username"),
            password=form.cleaned_data.get("password")
        )
        if user:
            login(request=request, user=user)
            messages.add_message(request=request, level=messages.SUCCESS, message="Ви війшли в аккаунт.")
            return redirect("index")
        else:
            messages.add_message(request=request, level=messages.ERROR, message="Помилка.")
            
    return render(request=request, template_name="sign_in.html", context=dict(form=form))

def product_list_cached(request):
    products = Product.objects.all()
    return render(request, "show_prod.html", {"products": products})

@login_required(login_url="/sign_up/")
def logout_func(request):
        logout(request)
        messages.success(request, "Ви успішно вийшли")
        return redirect("sign_in")
    

@login_required
@require_POST
def profile_post(request: HttpRequest):
    user_form = UserForm(data=request.POST, instance=request.user)
    profile_form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user.details)
    
    
    if profile_form.is_valid():
        messages.info(request, "Дані оновлені" )
    
    
    if  user_form.is_valid() and  user_form.changed_data:
            user_form.save()

        
    if profile_form.is_valid() and profile_form.changed_data:
            profile_form.save()
    
    else:
        messages.error(request, "Невірна каптча")
            
            
    return redirect("profile")