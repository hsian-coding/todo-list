from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
# Create your views here.


@login_required
def profile(request):
    return render(request, './user/profile.html', {'user': request.user})


@login_required
def user_logout(request):
    logout(request)

    return redirect('todo')


def user_login(request):
    message = ''
    if request.method == 'POST':
        if request.POST.get('register'):
            return redirect('register')
        if request.POST.get('login'):
            username = request.POST.get('username')
            password = request.POST.get('password')

            if username == '' or password == '':
                message = '帳號密碼不能為空!'
            else:
                user = authenticate(
                    request, username=username, password=password)
                if not user:
                    message = '帳號或密碼錯誤!'
                else:
                    message = '登入成功!'
                    login(request, user)
                    return redirect('todo')

    return render(request, './user/login.html', {'message': message})

# 註冊功能


def user_register(request):
    message = ''
    form = CustomUserForm()
    if request.method == 'POST':

        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        # 密碼問題
        if password1 != password2:
            message = '兩次密碼輸入不同!'
        elif len(password1) < 8:
            message = '密碼過短!'
        else:
            # 帳號問題
            if User.objects.filter(username=username).exists():
                message = '帳號重複!'
            else:
                user = User.objects.create_user(username=username,
                                                password=password1, email=email)
                message = '註冊失敗!'
                if user:
                    user.save()
                    message = '註冊成功!'
                    login(request, user)
                    return redirect('profile')

        print(username, password1, password2)
    return render(request, './user/register.html', {'form': form, 'message': message})
