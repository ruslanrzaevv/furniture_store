from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


from users.forms import UserLoginForm, UserRegistrtionForm, ProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, Вы вошли в аккаунт')

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('index'))
              
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }

    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrtionForm(data=request.POST)

        if form.is_valid():
            user = form.save()  
            auth.login(request, user)  
            return redirect('login')
    else:
        form = UserRegistrtionForm()
    
    context = {
        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'users/registr.html', context)


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)

        if form.is_valid():
            form.save() 
            messages.success(request, 'Профайл успешно обновлен.') 
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': 'Home - Кабинет',
        'form':form
    }
    return render(request, 'users/profile.html', context)


def users_cart(request):
    
    return render(request, 'users/users_cart.html')

def logout(request):
    messages.success(request, 'Вы вышли из акккаунта.') 
    auth.logout(request)
    return redirect('index')
