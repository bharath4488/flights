from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import *

from django.views.generic import ListView, DetailView

from math import sin, cos, sqrt, atan2, radians

import datetime


# Create your views here.


def airports_distance(latitude1, longitude1, latitude2, lonongitude2):

    R = 6373.0

    lat1 = radians(latitude1)
    lon1 = radians(longitude1)
    lat2 = radians(latitude2)
    lon2 = radians(lonongitude2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    

    return int(distance)

def getdatetime():
    currentdatetime = datetime.datetime.now()
    dt_string = currentdatetime.strftime("%d/%m/%Y %H:%M")
    return dt_string

def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('user_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use.')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')

        return redirect('login')
        
        

    else:    
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('User_Name')
        password = request.POST.get('Password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials, please try again.')
            return redirect('login')

    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def flightdetails(request):

    #recieving values from home page
    ok1 = request.session['origin']
    ok2 = request.session['destination']
    flighttype = request.session['radiobuttons']
    datetime = request.session['datepicker']
    totaladultpassengers = int(request.session['adultpassengers'])
    totalchildpassengers = int(request.session['childpassengers'])

    air_port1 = Airport.objects.get(city=ok1)
    
    airport1 = air_port1.airportname
    lat1 = float(air_port1.airportLatitude)
    lon1 = float(air_port1.airportLongitude)

    air_port2 = Airport.objects.get(city=ok2)
    airport2 = air_port2.airportname
    lat2 = float(air_port2.airportLatitude)
    lon2 = float(air_port2.airportLongitude)

    distance = airports_distance(lat1, lon1, lat2, lon2)
    adultbill = (distance * 5.5)*totaladultpassengers
    childbill = ((distance * 5.5)/2)*totalchildpassengers
    price = adultbill + childbill
    tax = (price*18)/100
    totalprice = price+tax

    #sending values to payments page
    request.session['adultbill'] = adultbill
    request.session['childbill'] = childbill
    request.session['price'] = price
    request.session['tax'] = tax
    request.session['totalprice'] = totalprice
    request.session['distance'] = distance

    context = {
        'ok1' : ok1,
        'ok2' : ok2,
        'airport1' : airport1,
        'airport2' : airport2,
        'flighttype' : flighttype,
        'datetime' : datetime,
        'distance': distance,
        'price': price,
        'totaladultpassengers': totaladultpassengers,
        'totalchildpassengers': totalchildpassengers
    }
    return render(request, 'flightdetails.html', context)

@login_required(login_url='login')
def flightshome(request):

    
    cities = Airport.objects.all()


    context = {
        'cities': cities,

    }

    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        radiobuttons = request.POST.get('exampleRadios')
        datepicker = request.POST.get('Datepicker')
        adultpassengers = request.POST.get('adults')
        childpassengers = request.POST.get('children')
        #sending values to flightdetals page
        request.session['origin'] = origin
        request.session['destination'] = destination
        request.session['radiobuttons'] = radiobuttons
        request.session['datepicker'] = datepicker
        request.session['adultpassengers'] = adultpassengers
        request.session['childpassengers'] = childpassengers

        return redirect('flightdetails')

    

    return render(request, 'flightshome.html', context)

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def payments(request):

    #recieving details from flight details
    adultscost = request.session['adultbill']
    childcost = request.session['childbill']
    totalbill = request.session['price']
    taxbill = request.session['tax']
    maxtotalbill = request.session['totalprice']
   
    ok1 = request.session['origin']
    ok2 = request.session['destination']
    flighttype = request.session['radiobuttons']
    datetime = request.session['datepicker']
    print(datetime)
    totaladultpassengers = int(request.session['adultpassengers'])
    totalchildpassengers = int(request.session['childpassengers'])
    distance = request.session['distance']

    context = {
        'adultscost': adultscost,
        'childcost': childcost,
        'totalbill': totalbill,
        'taxbill': taxbill,
        'maxtotalbill': maxtotalbill,
    }

    bookedon = getdatetime()
    User = request.user
    journey = (ok1 + " - " + ok2)

    if request.method == 'POST':
        flightbookingshistory.objects.create(user=User, journey=journey, journeydate=datetime, bookedon=bookedon, category=flighttype, total_price=maxtotalbill)
        
    return render(request, "payments.html", context)

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def contact(request):

    

    if request.method == 'POST':
        email = request.POST.get('email')
        subj = request.POST.get('subject')
        msg = request.POST.get('message')

        User_querie.objects.create(email=email, subject=subj, messsage=msg)
        

        

    return render(request, 'contact.html')

@login_required(login_url='login')
def archive(request):
    return render(request, 'archive.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def myflights(request):    
    matcheduser = flightbookingshistory.objects.filter(user=request.user)
    if len(matcheduser)==0:
        context = {
            'matcheduser': matcheduser
        }
    else:
        context = {
            'matcheduser': matcheduser
        }


    return render(request, 'myflights.html', context)

@login_required(login_url='login')
def profile(request):
    return render(request, 'profiles.html')


    poiname = request.session['poiname']
    poifilter = Points_of_Interest.objects.filter(Point_of_interest=poiname)
    context = {
        'poifilter': poifilter
    }
    return render(request, 'poidetailview.html', context)


class states(ListView):
    model = state
    template_name = 'states.html'

class placesofinterest(DetailView):
    model = Points_of_Interest
    template_name = 'placesofinterest.html'

class poidetailview(DetailView):
    model = Points_of_Interest
    template_name = 'poidetailview.html'
































































































def garbage(request):
    return render(request, 'garbage.html')