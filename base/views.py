from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import MyUserCreationForm

# Create your views here.
def default(request):
    return redirect('home')

def home(request):
    return render(request, 'home.html', {'page': 'home', 'cart': 0})

def shop(request):
    return render(request, 'shop.html', {'page': 'shop', 'cart': 0})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = MyUserCreationForm()

    if request.method == 'POST':
        type = request.POST.get('type')
        if type == 'login':
            email = request.POST.get('email'),
            password = request.POST.get('password')
    
            try:
                user = User.objects.get(email=email)
            except:
                print('something went wrong')
        
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('shop')
            else:
                print('something went wrong auth')
        else:
            form = MyUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('shop')
            else:
                print('registration error')

    return render(request, 'login.html', {'form': form, 'page': 'login'})

def product(request):
    return render(request, 'product_display.html', {})