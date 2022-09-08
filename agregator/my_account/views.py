from django.http import HttpResponse,HttpRequest, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login

from my_account.models import User, Post
from my_account.forms import UserLoginForm, UserSigupForm

def home(request):
    return render(request, "/home.html")


@csrf_exempt
def login(request):
    form = UserLoginForm(request.POST)

    if request.method == 'GET':
        return render(request, '/login.html', {'form': form})

    elif request.method == 'POST':
        if form.is_valid():
            username = form.clean_data['username']
            password = form.clean_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                django_login(request, user)
                return render(request, '/profile.html', context={'username': user.get_username()})

        return render(request, '/login.html', {'form': form, 'login_error_message': 'Error login'})

    return HttpResponseBadRequest('Error')


@csrf_exempt
def signup(request: HttpRequest):
    if request.method == 'GET':
        return render(request, '/signup.html')

    elif request.method == 'POST':
        form = UserSigupForm(request.POST)

        if form.is_valid():
            data = request.POST.dict()
            password = data.pop('password')

            user: User = User.objects.create(**data)
            user.set_password(password)
            user.save()

            User.objects.create(user=user)
            return render(request, '/login.html')
        else:
            context = {'error_message': form.errors}
            return render(request, '/signup.html', context)

    return HttpResponseBadRequest('Error')
