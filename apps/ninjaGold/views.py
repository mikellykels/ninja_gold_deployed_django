from django.shortcuts import render, redirect
from django.utils import timezone
import random
import datetime

now = timezone.now()


# Create your views here.

def index(request):
    if not request.session.get('gold'):
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'ninjaGold/index.html')

def process_money(request):
    if request.method == "POST":
        if request.POST['building'] == 'farm':
            request.session['building'] = random.randrange(9, 21)
            activity = {'activity': "Earned {} from the farm. {}".format(request.session['building'], now.strftime("%b %d, %Y %r, %Z")), 'class': "win"}
            print (request.session['activities'], datetime.datetime.now())
        elif request.POST['building'] == 'cave':
            request.session['building'] = random.randrange(6, 11)
            activity = {'activity': "Earned {} from the cave. {}".format(request.session['building'], now.strftime("%b %d, %Y %r, %Z")), 'class': "win"}
        elif request.POST['building'] == 'house':
            request.session['building'] = random.randrange(3, 6)
            activity = {'activity': "Earned {} from the house. {}".format(request.session['building'], now.strftime("%b %d, %Y %r, %Z")), 'class': "win"}
        elif request.POST['building'] == 'casino':
            request.session['building'] = random.randrange(-51, 51)
            if request.session['building'] >= 0:
                activity = {'activity': "Earned {} from the casino. {}".format(request.session['building'], now.strftime("%b %d, %Y %r, %Z")), 'class': "win"}
            if request.session['building'] <= 0:
                activity = {'activity': "Lost {} from the casino. {}".format(request.session['building'], now.strftime("%b %d, %Y %r, %Z")), 'class': "lose"}
        else:
            print ("lame")
    request.session['gold'] += request.session['building']

    request.session['activities'].append(activity)
    return redirect('/')

def reset(request):
    del request.session['building']
    del request.session['activities']
    del request.session['gold']
    return redirect('/')
