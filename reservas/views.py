from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import requires_csrf_token


def lotus_login(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'calendario.html', context=context)

    if request.method == "GET":
        context = {}
        return render(request, 'login.html', context=context)
    elif request.method == "POST":
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            context = {}
            return render(request, 'calendario.html', context=context)
        else:
            # Return an 'invalid login' error message.
            context={'msg_error':'Usuário e/ou senha desconhecido'}
            return render(request, 'login.html', context=context)

def lotus_logout(request):
    logout(request)
    context={}
    return render(request, 'login.html', context=context) 