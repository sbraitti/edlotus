from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import requires_csrf_token
from datetime import datetime
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .utils import Calendar

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


#Calendario


class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()